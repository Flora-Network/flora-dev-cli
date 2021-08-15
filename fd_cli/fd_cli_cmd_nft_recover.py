import click
import requests
import sqlite3
import urllib3

from chia.pools.pool_puzzles import (
    SINGLETON_MOD_HASH,
    create_p2_singleton_puzzle
)

from chia.util.bech32m import (
    decode_puzzle_hash
)

from chia.util.byte_types import (
    hexstr_to_bytes
)

from chia.util.ints import (
    uint64
)

from chia.types.blockchain_format.program import (
    Program,
    SerializedProgram
)

from chia.types.blockchain_format.sized_bytes import (
    bytes32
)

from fd_cli.fd_cli_assert import (
    fd_cli_assert_env_set
)

from fd_cli.fd_cli_cst import (
    FD_CLI_CST_AGGREGATED_SIGNATURE
)

from fd_cli.fd_cli_env import (
    FD_CLI_ENV_BC_DB_PATH,
    FD_CLI_ENV_WT_DB_PATH
)

from fd_cli.fd_cli_print import (
    fd_cli_print_raw,
    fd_cli_print_coin_lite_many,
    fd_cli_print_value
)


def fd_cli_cmd_nft_recover(
        ctx: click.Context,
        delay: int,
        launcher_hash: str,
        pool_contract_address: str,
        node_host: str,
        node_port: int,
        cert_path: str,
        cert_key_path: str,
        cert_ca_path: str
) -> None:
    pre: int = 1
    fd_cli_assert_env_set(FD_CLI_ENV_BC_DB_PATH)
    fd_cli_assert_env_set(FD_CLI_ENV_WT_DB_PATH)

    delay_u64: uint64 = uint64(delay)
    launcher_hash_b32: bytes32 = bytes32(hexstr_to_bytes(launcher_hash))
    contract_hash_b32: bytes32 = decode_puzzle_hash(pool_contract_address)

    program_puzzle_hex: str = None

    db_wallet_cursor: sqlite3.Cursor = ctx.obj['wt_db'].cursor()
    db_wallet_cursor.execute(
        "SELECT * "
        "FROM  derivation_paths")

    while True:
        derivation_paths: list = db_wallet_cursor.fetchmany(10)

        if len(derivation_paths) == 0:
            break

        for row in derivation_paths:
            puzzle_hash: str = row[2]
            puzzle_hash_b32: bytes32 = bytes32(hexstr_to_bytes(puzzle_hash))

            puzzle = create_p2_singleton_puzzle(
                SINGLETON_MOD_HASH,
                launcher_hash_b32,
                delay_u64,
                puzzle_hash_b32
            )

            if contract_hash_b32 == puzzle.get_tree_hash():
                program_puzzle_hex = bytes(SerializedProgram.from_program(puzzle)).hex()
                break

    if program_puzzle_hex is None:
        fd_cli_print_raw('A valid puzzle program could not be created for the given arguments and the selected wallet.',
                         pre=pre)
        return

    db_bc_cursor: sqlite3.Cursor = ctx.obj['bc_db'].cursor()
    db_bc_cursor.execute(
        f"SELECT * "
        f"FROM coin_record "
        f"WHERE spent == 0 "
        f"AND timestamp <= (strftime('%s', 'now') - {delay}) "
        f"AND puzzle_hash LIKE '{contract_hash}' "
        f"ORDER BY timestamp DESC")

    coin_records: list = db_bc_cursor.fetchall()

    if len(coin_records) == 0:
        fd_cli_print_raw(f'No coins are eligible for recovery yet.', pre=pre)
        return
    else:
        fd_cli_print_raw('Coins eligible for recovery:', pre=pre)
        fd_cli_print_coin_lite_many(coin_records, pre=pre + 1)

    coin_solutions: list[dict] = []

    for coin in coin_records:
        coin_parent: str = coin[6]
        coin_amount: int = int.from_bytes(coin[7], byteorder='big', signed=False)

        coin_solution_hex: str = bytes(SerializedProgram.from_program(
            Program.to([uint64(coin_amount), 0])
        )).hex()

        coin_solutions.append({
            'coin': {
                'amount': coin_amount,
                'parent_coin_info': coin_parent,
                'puzzle_hash': contract_hash
            },
            'puzzle_reveal': program_puzzle_hex,
            'solution': coin_solution_hex
        })

    balance_recovered: int = 0

    if not cert_ca_path:
        urllib3.disable_warnings()

    for coin_solutions_b in [coin_solutions[x:x + 50] for x in range(0, len(coin_solutions), 50)]:

        balance_batch: int = 0

        for coin_solution in coin_solutions_b:
            balance_batch += coin_solution['coin']['amount']

        try:
            response = requests.post(
                url=f'https://{node_host}:{node_port}/push_tx',
                cert=(cert_path, cert_key_path),
                verify=cert_ca_path if cert_ca_path else False,
                json={
                    'spend_bundle': {
                        'aggregated_signature': FD_CLI_CST_AGGREGATED_SIGNATURE,
                        'coin_solutions': coin_solutions_b
                    }
                })

            if response.status_code != 201 and response.status_code != 200:
                response.raise_for_status()

            fd_cli_print_raw(
                f'A new network transaction has been sent to recover a total of '
                f'{balance_batch / (10 ** 12):.12f} coins.',
                pre=pre)
            balance_recovered += balance_batch

        except Exception as e:
            fd_cli_print_raw(
                'An error occurred while sending the recovery transaction.', pre=pre)
            fd_cli_print_raw(e, pre=pre)

    if balance_recovered == 0:
        fd_cli_print_raw(
            'Coins could not be recovered. '
            'Please check your input parameters, network connection and try again.', pre=pre)
        return

    fd_cli_print_raw('', pre=pre)
    fd_cli_print_raw(f'Sent transactions to recover a total of '
                     f'{balance_recovered / (10 ** 12):.12f} coins.', pre=pre)
    fd_cli_print_raw(f'Coins should be spendable in few network confirmations.', pre=pre)

import click
import sqlite3

from fd_cli.fd_cli_assert import (
    fd_cli_assert_env_set
)

from fd_cli.fd_cli_env import (
    FD_CLI_ENV_BC_DB_PATH
)

from fd_cli.fd_cli_print import (
    fd_cli_print_none,
    fd_cli_print_coin_many
)


def fd_cli_cmd_coin(
        ctx: click.Context,
        by: str,
        value: str
):
    fd_cli_assert_env_set(FD_CLI_ENV_BC_DB_PATH)

    db_bc_cursor: sqlite3.Cursor = ctx.obj['bc_db'].cursor()
    coin_records: list = []

    if by == 'hash':
        db_bc_cursor.execute(
            f"SELECT * "
            f"FROM coin_record "
            f"WHERE coin_name LIKE '{value}%' "
            f"ORDER BY timestamp DESC")
        coin_records = db_bc_cursor.fetchall()

    if by == 'hash_parent':
        db_bc_cursor.execute(
            f"SELECT * "
            f"FROM coin_record "
            f"WHERE coin_parent LIKE '{value}%' "
            f"ORDER BY timestamp DESC")
        coin_records = db_bc_cursor.fetchall()

    if by == 'hash_puzzle':
        db_bc_cursor.execute(
            f"SELECT * "
            f"FROM coin_record "
            f"WHERE puzzle_hash LIKE '{value}%' "
            f"ORDER BY timestamp DESC")
        coin_records = db_bc_cursor.fetchall()

    if coin_records is None or len(coin_records) == 0:
        fd_cli_print_none(pre=1)
        return

    fd_cli_print_coin_many(coin_records, pre=0)

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
    fd_cli_print_block_many
)


def fd_cli_cmd_block(
        ctx: click.Context,
        by: str,
        value: str
) -> None:
    fd_cli_assert_env_set(FD_CLI_ENV_BC_DB_PATH)

    db_bc_cursor: sqlite3.Cursor = ctx.obj['bc_db'].cursor()
    block_records: list = []

    if by == 'height':
        db_bc_cursor.execute(
            f"SELECT * "
            f"FROM full_blocks "
            f"WHERE height == {int(value)} "
            f"ORDER BY height DESC")
        block_records = db_bc_cursor.fetchall()

    if by == 'hash':
        db_bc_cursor.execute(
            f"SELECT * "
            f"FROM full_blocks "
            f"WHERE header_hash LIKE '{value}%' "
            f"ORDER BY height DESC")
        block_records = db_bc_cursor.fetchall()

    if block_records is None or len(block_records) == 0:
        fd_cli_print_none(pre=1)
        return

    fd_cli_print_block_many(block_records, pre=0)

import sqlite3


def fd_cli_db_get_connection(
        path: str
) -> sqlite3.Connection:
    return sqlite3.connect(
        f'file:{path}?mode=ro',
        uri=True
    )

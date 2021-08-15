import click

from fd_cli.fd_cli_print import (
    fd_cli_print_raw
)

from fd_cli.fd_cli_version import (
    FD_CLI_VERSION
)


def fd_cli_cmd_version(
        ctx: click.Context
) -> None:
    fd_cli_print_raw(FD_CLI_VERSION)

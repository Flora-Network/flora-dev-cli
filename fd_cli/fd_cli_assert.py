import os

from fd_cli.fd_cli_print import (
    fd_cli_print_require_env
)


def fd_cli_assert_env_set(
        env: str
) -> None:
    if env not in os.environ:
        fd_cli_print_require_env(env)
        exit(1)

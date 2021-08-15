import os
import click

from fd_cli.fd_cli_db import (
    fd_cli_db_get_connection
)

from fd_cli.fd_cli_env import (
    FD_CLI_ENV_BC_DB_PATH,
    FD_CLI_ENV_WT_DB_PATH
)

from fd_cli.fd_cli_cmd_coin import (
    fd_cli_cmd_coin
)

from fd_cli.fd_cli_cmd_block import (
    fd_cli_cmd_block
)

from fd_cli.fd_cli_cmd_nft_recover import (
    fd_cli_cmd_nft_recover
)

from fd_cli.fd_cli_cmd_version import (
    fd_cli_cmd_version
)


@click.group(
    context_settings={}
)
@click.pass_context
def fd_cli(
        ctx: click.Context,
) -> None:
    ctx.ensure_object(dict)

    if FD_CLI_ENV_BC_DB_PATH in os.environ:
        ctx.obj['bc_db'] = fd_cli_db_get_connection(os.environ[FD_CLI_ENV_BC_DB_PATH])
    else:
        ctx.obj['bc_db'] = None

    if FD_CLI_ENV_WT_DB_PATH in os.environ:
        ctx.obj['wt_db'] = fd_cli_db_get_connection(os.environ[FD_CLI_ENV_WT_DB_PATH])
    else:
        ctx.obj['wt_db'] = None


def fd_cli_assert_env_set(
        env: str
) -> None:
    if env not in os.environ:
        fd_cli_print_require_env(env)
        exit(1)


@fd_cli.command(
    'block',
    help='Retrieve block data.'
)
@click.option(
    '-b',
    '--by',
    required=True,
    type=click.Choice(
        [
            'hash',
            'height',
        ],
        case_sensitive=False
    ),
    help="Interpret 'value' as."
)
@click.argument(
    'value',
    required=True
)
@click.pass_context
def fd_cli_block(
        ctx: click.Context,
        by: str,
        value: str
) -> None:
    fd_cli_cmd_block(
        ctx=ctx,
        by=by,
        value=value
    )


@fd_cli.command(
    'coin',
    help='Retrieve coin data.'
)
@click.option(
    '-b',
    '--by',
    required=True,
    type=click.Choice(
        [
            'hash',
            'hash_parent',
            'hash_puzzle'
        ],
        case_sensitive=False
    ),
    help="Interpret 'value' as."
)
@click.argument(
    'value',
    required=True
)
@click.pass_context
def fd_cli_coin(
        ctx: click.Context,
        by: str,
        value: str
) -> None:
    fd_cli_cmd_coin(
        ctx=ctx,
        by=by,
        value=value
    )


@fd_cli.command(
    'nft-recover',
    help="NFT prizes recovery."
)
@click.option(
    '-d',
    '--delay',
    required=True,
    type=int,
    default=604800,
    show_default=True
)
@click.option(
    '-l',
    '--launcher_hash',
    required=True,
    type=str
)
@click.option(
    '-c',
    '--contract_hash',
    required=True,
    type=str
)
@click.option(
    '-nh',
    '--node-host',
    required=True,
    type=str
)
@click.option(
    '-np',
    '--node-port',
    required=True,
    type=int,
)
@click.option(
    '-ct',
    '--cert-path',
    required=True,
    type=str
)
@click.option(
    '-ck',
    '--cert-key-path',
    required=True,
    type=str
)
@click.option(
    '-ca',
    '--cert-ca-path',
    required=False,
    type=str,
)
@click.pass_context
def fd_cli_nft_recover(
        ctx: click.Context,
        delay: int,
        launcher_hash: str,
        contract_hash: str,
        node_host: str,
        node_port: int,
        cert_path: str,
        cert_key_path: str,
        cert_ca_path: str
) -> None:
    fd_cli_cmd_nft_recover(
        ctx=ctx,
        delay=delay,
        launcher_hash=launcher_hash,
        contract_hash=contract_hash,
        node_host=node_host,
        node_port=node_port,
        cert_path=cert_path,
        cert_key_path=cert_key_path,
        cert_ca_path=cert_ca_path
    )


@fd_cli.command(
    'version',
    help='Retrieve version.'
)
@click.pass_context
def fd_cli_version(
        ctx: click.Context
) -> None:
    fd_cli_cmd_version(
        ctx=ctx
    )


def main() -> None:
    fd_cli()


if __name__ == '__main__':
    fd_cli()

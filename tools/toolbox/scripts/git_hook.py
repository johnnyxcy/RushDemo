#!/usr/bin/python
import os
import platform
import subprocess
import sys
import json
import pathlib

_toolbox_root = pathlib.Path(__file__).parent.parent
sys.path.append(_toolbox_root.as_posix())

from utils.argparser_utils import ArgumentParser
from utils.logging_utils import logger


def git_hook(hook: str) -> None:

    pkg = _toolbox_root.joinpath('package.json')
    if not pkg.exists():
        raise FileNotFoundError(
            f'Package.json not found in {pkg.parent.as_posix()}')

    hooks = json.loads(open(pkg, encoding='utf-8').read()).get('gitHooks')
    if not hooks:
        logger.debug('No gitHooks found')
        exit(0)

    command: str = hooks.get(hook, None)
    if not command:
        logger.debug(f'No gitHooks for {hook} found')
        exit(0)

    node_modules_bin = _toolbox_root.joinpath("node_modules/.bin").absolute()

    logger.info(f'>> Running {hook} hook: {command}')

    env_path: str = os.environ['PATH']
    if platform.system() == 'Windows':
        env_path = f'{node_modules_bin.as_posix()};{env_path}'
    elif platform.system() == 'Darwin':
        env_path = f'{node_modules_bin.as_posix()}:{env_path}'
    else:
        raise NotImplementedError(f'{platform.system} is not supported yet')

    os.environ['PATH'] = env_path

    try:
        subprocess.check_call(command, shell=True, env=os.environ)
    except Exception as e:
        logger.error(e)
        exit(1)


def cli() -> None:
    parser = ArgumentParser(
        description=
        '[toolbox.scripts.git_hook] - process git hooks with configured "gitHooks" arguments in package.json'
    )
    parser.add_argument(
        'HOOK',
        type=str,
        help=
        'Name of the git hook, such as `pre-commit` or `commit-msg`, see README.md for more details'
    )
    parsed_args = parser.parse_args()
    git_hook(hook=parsed_args.HOOK)


if __name__ == '__main__':
    cli()

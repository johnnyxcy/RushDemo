#!/usr/bin/python

import pathlib
import sys

_toolbox_root = pathlib.Path(__file__).parent.parent
sys.path.append(_toolbox_root.as_posix())

from src.git_hook_parser import cli

if __name__ == '__main__':
    cli()

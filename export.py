#!/usr/bin/env python3

import os
import subprocess
import json
from pathlib import Path
import sys

args = sys.argv[1]

def export_passwords(args):
    export = []
    if not args: 
        pass_base_path = _get_pass_base_path()
    else:
        pass_base_path = str(_get_pass_base_path()) + args

    def return_pass_paths(path):
        pass_paths = []
        for p in Path(path).rglob('*.gpg'):
            pass_paths.append(str(p.relative_to(path)).replace(".gpg", ""))
            # print(result.replace(path, "").replace("/", "", 1))
        return pass_paths
    # print(return_pass_paths(pass_base_path)[5])
    # print(_get_password_from_pass(return_pass_paths(pass_base_path)[3]))
    for i in return_pass_paths(pass_base_path):
        print(i)



def _get_password_from_pass(pass_path: str) -> str:
    """Get the pasword from pass."""
    return subprocess.check_output(['pass', pass_path]).decode().splitlines()[0]

def _get_pass_base_path() -> str:
    """Get the path of the password store."""
    return os.environ.get('PASSWORD_STORE_DIR', os.path.expanduser(
        '~/.password-store'))

export_passwords()

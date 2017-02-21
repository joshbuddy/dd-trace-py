#!/usr/bin/env python
from __future__ import print_function

import os
import sys


USAGE = """
Usage: ddtrace-run [ENV_VARS] <my_program>
"""

def _ddtrace_root():
    from ddtrace import __file__
    return os.path.dirname(__file__)

def _add_bootstrap_to_pythonpath(bootstrap_dir):
    python_path = bootstrap_dir
    if 'PYTHONPATH' in os.environ:
        path = os.environ['PYTHONPATH'].split(os.path.pathsep)
        if bootstrap_dir not in path:
            python_path = "%s%s%s" % (bootstrap_dir, os.path.pathsep,
                    os.environ['PYTHONPATH'])

    os.environ['PYTHONPATH'] = python_path


def main():
    root_dir = _ddtrace_root()
    bootstrap_dir = os.path.join(root_dir, 'bootstrap')

    _add_bootstrap_to_pythonpath(bootstrap_dir)
    if len(sys.argv) < 2:
        print(USAGE)
        return

    program_exe_path = sys.argv[1]
    # Find the executable path
    if not os.path.dirname(program_exe_path):
        program_search_path = os.environ.get('PATH', '').split(os.path.pathsep)
        for path in program_search_path:
            path = os.path.join(path, program_exe_path)
            if os.path.exists(path) and os.access(path, os.X_OK):
                program_exe_path = path
                break

    print("argv:", sys.argv)
    print("pythonpath:", os.environ['PYTHONPATH'])
    print("program path:", program_exe_path)

    if 'DATADOG_SERVICE_NAME' not in os.environ:
        # infer service name from program command-line
        service_name = os.path.basename(program_exe_path)
        os.environ['DATADOG_SERVICE_NAME'] = service_name

    os.execl(program_exe_path, program_exe_path, *sys.argv[2:])

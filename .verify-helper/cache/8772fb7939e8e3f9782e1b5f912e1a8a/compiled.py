#!/usr/local/opt/python@3.11/bin/python3.11
"""This is a helper script to run the target Python code.

We need this script to set PYTHONPATH portably. The env command, quoting something, etc. are not portable or difficult to implement.
"""

import os
import sys

# arguments
path = '/Users/osanai/Documents/GitHub/python-library/library_checker/data_structure/static_range_sum.test.py'
basedir = '/Users/osanai/Documents/GitHub/python-library'

# run library_checker/data_structure/static_range_sum.test.py
env = dict(os.environ)
if "PYTHONPATH" in env:
    env["PYTHONPATH"] = basedir + os.pathsep + env["PYTHONPATH"] 
else:
    env["PYTHONPATH"] = basedir  # set `PYTHONPATH` to import files relative to the root directory
os.execve(sys.executable, [sys.executable, path], env=env)  # use `os.execve` to avoid making an unnecessary parent process

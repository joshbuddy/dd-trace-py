#!/usr/bin/env python
import os
import sys

import subprocess
import unittest


class DdtraceRunTest(unittest.TestCase):
    def test_service_name_default(self):
        out = subprocess.check_output(
            ['ddtrace-run', 'python', 'tests/scripts/ddtrace_run_env.py']
        )
        assert out.startswith("Test success")

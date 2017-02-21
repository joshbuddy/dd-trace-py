#!/usr/bin/env python
import os
import sys

import subprocess
import unittest


class DdtraceRunTest(unittest.TestCase):
    def test_service_name_default(self):
        out = subprocess.check_output(
            ['ddtrace-run', 'python', 'tests/scripts/ddtrace_run_service.py']
        )
        assert out.startswith("Test success")

    def test_env_name_passthrough(self):
        os.environ["DATADOG_ENV"] = "test"
        out = subprocess.check_output(
            ['ddtrace-run', 'python', 'tests/scripts/ddtrace_run_env.py']
        )
        assert out.startswith("Test success")

    def test_env_enabling(self):
        os.environ["DATADOG_TRACE_ENABLED"] = "false"
        out = subprocess.check_output(
            ['ddtrace-run', 'python', 'tests/scripts/ddtrace_run_disabled.py']
        )
        assert out.startswith("Test success")

        os.environ["DATADOG_TRACE_ENABLED"] = "true"
        out = subprocess.check_output(
            ['ddtrace-run', 'python', 'tests/scripts/ddtrace_run_enabled.py']
        )
        assert out.startswith("Test success")

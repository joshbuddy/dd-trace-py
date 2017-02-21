from __future__ import print_function

from ddtrace import tracer
import os

if __name__ == '__main__':
    assert os.environ['DATADOG_SERVICE_NAME'] == 'python'
    print("Test success")

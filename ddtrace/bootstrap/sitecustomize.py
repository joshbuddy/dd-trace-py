from __future__ import print_function

"""
Bootstrapping code that is run when using the `ddtrace-run` Python entrypoint
Add all monkey-patching that needs to run by default here
"""

try:
    from ddtrace import patch_all; patch_all(django=True, flask=True, pylons=True) # noqa
    from ddtrace import tracer
    import os

    if 'DATADOG_SERVICE_ENV' in os.environ:
        tracer.set_tags({"env": os.environ["DATADOG_SERVICE_ENV"]})
except Exception as e:
    print("error configuring Datadog tracing")

from ndk.devenv.devices import DeviceConfig
from ndk.devenv.testrunner.case import TestCase


def run_unsupported(test: TestCase, device: DeviceConfig) -> str | None:
    # Static-executable tests are broken on old kernels, rather than by API
    # levels. Marking unsupported prior to API 34, the first API level without
    # kernels less than 4.14 (b/502794163).
    if test.name == "wait.test_wait-static" and device.version < 34:
        return f"{device.version}"
    return None

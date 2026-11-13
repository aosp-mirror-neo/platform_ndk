import ndk.abis
from ndk.devenv.devices import DeviceConfig
from ndk.devenv.testrunner.case import TestCase
from ndk.test.buildtest.case import Test


def extra_cmake_flags() -> list[str]:
    # Required for static executables.
    return ["-DANDROID_PLATFORM=latest"]


def override_runtime_minsdkversion(test: Test) -> int | None:
    # We build as latest because static executables require that, but static executables
    # are compatible with old OS versions.
    return ndk.abis.min_api_for_abi(test.config.abi)


def run_unsupported(_test: TestCase, device: DeviceConfig) -> str | None:
    # Static-executable tests are broken on old kernels, rather than by API
    # levels. Marking unsupported prior to API 34, the first API level without
    # kernels less than 4.14 (b/502794163).
    if device.version < 34:
        return f"{device.version}"
    return None

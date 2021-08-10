import pkg_resources
import subprocess
import sys


def get_bin_name(platform: str) -> str:
    if platform == "darwin":
        return "bin/c_test_macos"
    elif platform == "linux":
        return "bin/c_test_linux"
    else:
        raise ValueError("Unsupported platform")


def multiply_ext(lhs: int, rhs: int) -> int:
    res = subprocess.run(
        [
            pkg_resources.resource_filename("py_ext_test", get_bin_name(sys.platform)),
            str(lhs),
            str(rhs),
        ],
        capture_output=True,
        text=True,
    )

    if res.returncode != 0:
        raise ValueError("Problem with args")

    return int(res.stdout)

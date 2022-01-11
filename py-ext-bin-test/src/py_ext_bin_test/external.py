import subprocess
import sys

import pkg_resources


def get_bin_path(package_name: str, name: str) -> str:
    bin_name = name
    if sys.platform == "win32":
        bin_name = bin_name + ".exe"

    return pkg_resources.resource_filename(package_name, f"bin/{bin_name}")


def multiply_ext(lhs: int, rhs: int) -> int:
    res = subprocess.run(
        [
            get_bin_path("py_ext_bin_test", "c_test"),
            str(lhs),
            str(rhs),
        ],
        capture_output=True,
        text=True,
    )

    if res.returncode != 0:
        raise ValueError("Problem with args")

    return int(res.stdout)

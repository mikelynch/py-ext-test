import pkg_resources
import subprocess


def multiply_ext(lhs: int, rhs: int) -> int:
    res = subprocess.run(
        [
            pkg_resources.resource_filename("py_ext_test", "bin/c_test"),
            str(lhs),
            str(rhs),
        ],
        capture_output=True,
        text=True,
    )

    if res.returncode != 0:
        raise ValueError("Problem with args")

    return int(res.stdout)

import pkg_resources
import subprocess


def fibo(pos: int) -> int:
    # We could load the resource directly,
    # but want to be able to demonstrate using it
    # with its path too.

    if pos > 12:
        raise ValueError("Problem with args")

    res = subprocess.run(
        "sed '{}q;d' '{}'".format(
            pos + 1,
            pkg_resources.resource_filename("py_ext_data_test", "data/fibo.txt"),
        ),
        shell=True,
        capture_output=True,
        text=True,
    )

    if res.returncode != 0:
        raise ValueError("Problem with args")

    return int(res.stdout)

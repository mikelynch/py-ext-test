import pkg_resources


def fibo(pos: int) -> int:
    # We could load the resource directly,
    # but want to be able to demonstrate using it
    # with its path too.
    with open(pkg_resources.resource_filename("py_ext_data_test", "data/fibo.txt")) as f:
        lines = [int(line) for line in f.readlines()]

    if pos > len(lines):
        raise ValueError("Problem with args")

    return lines[pos]

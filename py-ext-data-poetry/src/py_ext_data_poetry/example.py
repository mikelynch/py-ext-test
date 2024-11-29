import pkgutil


def fibo(pos: int) -> int:
    # We could load the resource directly,
    # but want to be able to demonstrate using it
    # with its path too.
    lines = [
        int(line)
        for line in pkgutil.get_data("py_ext_data_poetry", "data/fibo.txt")
        .decode("utf-8")
        .split("\n")
        if line
    ]

    if pos > len(lines):
        raise ValueError("Problem with args")

    return lines[pos]

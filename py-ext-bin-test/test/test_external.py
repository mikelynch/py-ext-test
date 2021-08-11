import py_ext_bin_test.external


def test_a():
    assert 6 == py_ext_bin_test.example.multiply(2, 3)

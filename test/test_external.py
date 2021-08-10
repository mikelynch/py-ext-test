import py_ext_test.external


def test_a():
    assert 6 == py_ext_test.example.multiply(2, 3)

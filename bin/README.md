# External binary

This is a simple program
that outputs the product of two numbers,
used for the `py_ext_bin_test` example.

To build this on Linux/macOS systems run:
```bash
gcc c_test.c -o <platform>/c_test
```

This includes:
* `manylinux2014`
* `manylinux_2_28`
* `manylinux_2_34`
* `musllinux_1_2`

These are built using the [manylinux images](https://github.com/pypa/manylinux)
for x64 and AArch64 architectures.

On Windows,
run the following
and copy to the appropriate location:
```
cl c_test.c
```

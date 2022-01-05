# Bundling external dependencies in Python packages

This repo contains two Python packages
that demonstrate how to integrate external dependencies
into the built wheel:
* Binaries
* Data files

These two use cases can of course be combined.

## Bundling binaries (`py-ext-bin-test`)

This shows how to bundle binaries,
which can then be used from the package.

There are two broad ways this could be achieved:
1. Bundle binaries for all supported platforms
  and make a general wheel.
  This makes for large wheels (as include multiple platforms)
  and requires that the user select the right binary at runtime.
2. Bundle only the appropriate binaries
  and make multiple platform-specific wheels.
  This is slightly more complicated to set up,
  but only includes the binaries needed for a particular platform,
  and simplifies the use at runtime.

This packages uses the latter approach.

There is an example binary in `bin`,
which simply calculates the product of two arguments passed to it,
and is compiled for a few different platforms.

`py_ext_bin_test.external` demonstrates how to
call out to the bundled binary.

While it is likely possible to come up with
a pure Python/setuptools approach to this,
this package currently uses a Makefile.

At build time,
this copies the contents of `bin/<platform>`
so that the wheel contains only the desired binaries
at `py_ext_bin_test/bin`.

## Bundling data (`py-ext-data-test`)

This shows how to bundle data files
within a Python package.

This use case is more straightforward,
but some of the documentation online
is quite out of date,
so this shows a complete example of how to do it.

It also shows how to support
including files from outside the package tree,
or even outside the repo.
Here, this is represented by the contents of `ext-data`.

Once again, this uses a Makefile to perform the necessary steps.
At build time,
this copies the contents of `ext_data`
into `py_ext_data_test/data`.

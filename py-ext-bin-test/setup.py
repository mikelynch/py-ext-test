import os
from distutils.dist import Distribution
from setuptools import find_packages, setup
from wheel.bdist_wheel import bdist_wheel


# Get platform
default_platform = bdist_wheel(Distribution()).get_tag()[2]
platform = os.environ.get("PLATFORM", default_platform)


class BdistWheel(bdist_wheel):
    def finalize_options(self):
        super().finalize_options()
        self.root_is_pure = False

    def get_tag(self):
        python, abi = "py3", "none"
        return python, abi, platform


setup(
    name="py_ext_bin_test",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">3.5",
    package_data={
        "py_ext_bin_test": ["bin/*"],
    },
    cmdclass={
        "bdist_wheel": BdistWheel,
    },
)

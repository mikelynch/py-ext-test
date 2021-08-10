from setuptools import find_packages, setup


setup(
    name="py_ext_test",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">3.5",
    package_data={
        "py_ext_test": ["bin/*"],
    },
)

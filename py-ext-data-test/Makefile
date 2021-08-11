# Python environment to build in (requires setuptools, wheel and build)
PYTHON_ENV := ./.py

# Directory containing data (could be outside repo)
EXT_DATA := ../ext_data

# Directory to copy data into at build time
DATA_DIR := src/py_ext_data_test/data

.PHONY: data_dir
data_dir:
	mkdir -p $(DATA_DIR)/
	rm -f $(DATA_DIR)/*

wheel: data_dir
	cp -R $(EXT_DATA)/* $(DATA_DIR)/
	$(PYTHON_ENV)/bin/python -m build

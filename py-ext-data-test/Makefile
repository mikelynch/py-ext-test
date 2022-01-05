# Directory containing data (could be outside repo)
EXT_DATA := ../ext_data

# Directory to copy data into at build time
DATA_DIR := src/py_ext_data_test/data

.PHONY: data_dir
data_dir:
	mkdir -p $(DATA_DIR)/
	rm -f $(DATA_DIR)/*

wheel: data_dir
	rm -r build/ || true
	cp -R $(EXT_DATA)/* $(DATA_DIR)/
	python -m build

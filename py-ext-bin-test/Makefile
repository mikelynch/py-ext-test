# Python environment to build in (requires setuptools, wheel and build)

# Directory containing binaries (could be outside repo)
EXT_BIN := ../bin

# Directory to copy binaries into at build time
BIN_DIR := src/py_ext_bin_test/bin

.PHONY: bin_dir
bin_dir:
	mkdir -p $(BIN_DIR)/
	rm -f $(BIN_DIR)/*

manylinux1_x86_64: bin_dir
	rm -r build/ || true
	cp $(EXT_BIN)/manylinux1_x86_64/* $(BIN_DIR)/
	PLATFORM=manylinux1_x86_64 python -m build

macosx_10_9_x86_64: bin_dir
	rm -r build/ || true
	cp $(EXT_BIN)/macosx_10_9_x86_64/* $(BIN_DIR)/
	PLATFORM=macosx_10_9_x86_64 python -m build

win_amd64: bin_dir
	rm -r build/ || true
	cp $(EXT_BIN)/win_amd64/* $(BIN_DIR)/
	PLATFORM=win_amd64 python -m build

all: manylinux1_x86_64 macosx_10_9_x86_64 win_amd64

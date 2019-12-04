# %%
import os
import shutil
import pathlib
import pandas as pd
from data_science_toolbox.io.directory_tree import directory_tree

TEST_DIR_CREATE = pathlib.Path('tests/io/directory_tree_test_files')
TEST_SUBDIR_CREATE = pathlib.Path(
    'tests/io/directory_tree_test_files/subdirectory')

TEST_FNAMES = ['test_fname_1.txt',
               'test_fname_2.txt', ]


def test_file_search_and_replace():
    # Create test dir
    if not os.path.exists(TEST_DIR_CREATE.as_posix()):
        os.mkdir(TEST_DIR_CREATE.as_posix())
    if not os.path.exists(TEST_SUBDIR_CREATE.as_posix()):
        os.mkdir(TEST_SUBDIR_CREATE.as_posix())
    # Create test filenames
    for test_file in TEST_FNAMES:
        if not os.path.exists(TEST_DIR_CREATE / test_file):
            with open(TEST_DIR_CREATE / test_file, 'w'):
                pass
        if not os.path.exists(TEST_SUBDIR_CREATE / test_file):
            with open(TEST_SUBDIR_CREATE / test_file, 'w'):
                pass

    # Check the directory is correct
    assert repr(directory_tree(TEST_DIR_CREATE)) == "'\\n+ " + \
        "tests\\\\io\\\\directory_tree_test_files\\n" \
        + "    + subdirectory\\n        + test_fname_1.txt\\n" \
        + "        + test_fname_2.txt\\n    + test_fname_1.txt\\n" \
        + "    + test_fname_2.txt'"

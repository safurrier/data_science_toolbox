# %%
import os
import shutil
import pathlib
import pandas as pd
import pytest
from data_science_toolbox.io.directory_tree import directory_tree


# NOTE
# This tests against a string literal
# Adding more test cases would require parameterizing
# assertion check solution

@pytest.mark.parametrize("create_dir, create_sub_dir, create_fnames_list",
                         [('tests/io/directory_tree_test_files',
                           'tests/io/directory_tree_test_files/subdirectory',
                           ['test_fname_1.txt',
                            'test_fname_2.txt', ],)
                          ]
                         )
def test_directory_tree(create_dir, create_sub_dir, create_fnames_list):
    # Pathlib.Path directories
    create_dir = pathlib.Path(create_dir)
    create_sub_dir = pathlib.Path(create_sub_dir)
    # Create test dir
    if not os.path.exists(create_dir.as_posix()):
        os.mkdir(create_dir.as_posix())
    if not os.path.exists(create_sub_dir.as_posix()):
        os.mkdir(create_sub_dir.as_posix())
    # Create test filenames
    for test_file in create_fnames_list:
        if not os.path.exists(create_dir / test_file):
            with open(create_dir / test_file, 'w'):
                pass
        if not os.path.exists(create_sub_dir / test_file):
            with open(create_sub_dir / test_file, 'w'):
                pass

    # Check the directory is correct
    assert repr(directory_tree(create_dir)) == "'\\n+ " + \
        "tests\\\\io\\\\directory_tree_test_files\\n" \
        + "    + subdirectory\\n        + test_fname_1.txt\\n" \
        + "        + test_fname_2.txt\\n    + test_fname_1.txt\\n" \
        + "    + test_fname_2.txt'"

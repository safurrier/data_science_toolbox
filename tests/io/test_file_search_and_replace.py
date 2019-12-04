# %%
import os
import shutil
import pathlib
import pandas as pd
from data_science_toolbox.io.file_search_and_replace import file_search_and_replace

DATA_FPATH = 'tests/io/data/test_df_dict.xlsx'
TEST_ALL_SHEETS = ['one', 'two', 'three']
TEST_SHEETS_INCLUDE = ['one', 'three']
TEST_SHEETS_EXCLUDE = ['two']

#########
# WARNING
#########

# The directory specified by TEST_DIR_CREATE
# Will be created and destroyed.
# Do not set it to any directory containing files
# you do not wish deleted

TEST_DIR_CREATE = pathlib.Path('tests/io/search_and_replace_test_files')


TEST_SEARCH_FNAMES = ['incorrect_fname_1.txt',
                      'incorrect_fname_2.txt',
                      'correct_fname_3.txt']

TEST_REPLACED_FNAMES = ['correct_fname_1.txt',
                        'correct_fname_2.txt',
                        'correct_fname_3.txt']

TEST_SEARCH_PHRASE = 'incorrect'
TEST_REPLACE_PHRASE = 'correct'


def test_file_search_and_replace():
    # Create test dir
    if not os.path.exists(TEST_DIR_CREATE.as_posix()):
        os.mkdir(TEST_DIR_CREATE.as_posix())
    # Create test filenames
    for test_file in TEST_SEARCH_FNAMES:
        if not os.path.exists(TEST_DIR_CREATE / test_file):
            with open(TEST_DIR_CREATE / test_file, 'w'):
                pass

    # Search and replace
    file_search_and_replace(TEST_DIR_CREATE.as_posix(),
                            TEST_SEARCH_PHRASE,
                            TEST_REPLACE_PHRASE)

    # Get filenames
    replaced_fnames = os.listdir(TEST_DIR_CREATE.as_posix())
    # Remove directory and files
    shutil.rmtree(TEST_DIR_CREATE.as_posix())

    # Assert have been correctly replaced
    assert not set(TEST_REPLACED_FNAMES).difference(replaced_fnames)

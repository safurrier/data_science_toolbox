# %%
import os
import shutil
import pathlib
import pandas as pd
import pytest
from data_science_toolbox.io.file_search_and_replace import file_search_and_replace

# The directory specified by 'create_dir'
# Will be created and destroyed.
# Do not set it to any directory containing files
# you do not wish deleted
# Note: 'create_dir' is the first item in the test case arg list

# Form of individual test case is
# (create_dir,
# test_search_fnames,
# test_replaced_fnames,
# search_phrase,
# replace_phrase)

FILE_SEARCH_AND_REPLACE_TEST_CASES = [
    ('tests/io/search_and_replace_test_files',
     ['incorrect_fname_1.txt',
      'incorrect_fname_2.txt',
      'correct_fname_3.txt'],
     ['correct_fname_1.txt',
      'correct_fname_2.txt',
      'correct_fname_3.txt'],
     'incorrect',
     'correct',
     ),
    ('tests/io/search_and_replace_test_files',
     ['broken_fname_1.txt',
      'brokenfname_2.txt',
      'fixed3.txt'],
     ['fixed_fname_1.txt',
      'fixedfname_2.txt',
      'fixed3.txt'],
     'broken',
     'fixed',
     ),
]


@pytest.mark.parametrize("""create_dir,
                         test_search_fnames, test_replaced_fnames,
                         search_phrase, replace_phrase""",
                         FILE_SEARCH_AND_REPLACE_TEST_CASES
                         )
def test_file_search_and_replace(create_dir,
                                 test_search_fnames, test_replaced_fnames,
                                 search_phrase, replace_phrase):
    # pathlib.Path the create directory
    create_dir = pathlib.Path(create_dir)
    # Create test dir
    if not os.path.exists(create_dir.as_posix()):
        os.mkdir(create_dir.as_posix())
    # Create test filenames
    for test_file in test_search_fnames:
        if not os.path.exists(create_dir / test_file):
            with open(create_dir / test_file, 'w'):
                pass

    # Search and replace
    file_search_and_replace(create_dir.as_posix(),
                            search_phrase,
                            replace_phrase)

    # Get filenames
    replaced_fnames = os.listdir(create_dir.as_posix())

    # Remove directory and files
    shutil.rmtree(create_dir.as_posix())

    # Assert have been correctly replaced
    assert not set(test_replaced_fnames).difference(replaced_fnames)

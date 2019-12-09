# %%
import os
import shutil
import pytest
import pathlib
from data_science_toolbox.io.unique_path import unique_path


UNIQUE_FPATH_TEST_CASES = [
    ('test_file_{:02d}.txt',
     'tests/io/unique_path_files',
     ['test_file_00.txt',
      'test_file_01.txt',
      ],
     'tests/io/unique_path_files/test_file_02.txt'
     ),
]


@pytest.mark.parametrize("fname_pattern, create_dir, create_fnames_list, assert_fname",
                         UNIQUE_FPATH_TEST_CASES
                         )
def test_get_absolute_fpath(fname_pattern, create_dir, create_fnames_list, assert_fname):
    # Pathlib.Path directories
    create_dir = pathlib.Path(create_dir)
    # Create test dir
    if not os.path.exists(create_dir.as_posix()):
        os.mkdir(create_dir.as_posix())

    # Create test filenames
    for test_file in create_fnames_list:
        if not os.path.exists(create_dir / test_file):
            with open(create_dir / test_file, 'w'):
                pass
    # Pull unique fpath
    unique_path_to_test = unique_path(create_dir, fname_pattern)

    # Remove directory and files
    shutil.rmtree(create_dir.as_posix())

    assert unique_path_to_test.as_posix() == assert_fname

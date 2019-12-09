# %%
import os
import shutil
import pytest
import pathlib
from data_science_toolbox.io.config_dict_from_python_fpath import config_dict_from_python_fpath


PYTHON_CONFIG_DICT_TEST_CASES = [
    (
        'tests/io/python_config_dicts/test_config_1.py',
        False,
        {'VAR_STR': 'testing',
         'VAR_LIST': ['a', 'b', 'c'],
         'VAR_DICT':{'sample': 100}
         }
    ),
    (
        'tests/io/python_config_dicts/test_config_2.py',
        False,
        {'VAR_STR': 'alternate',
         'VAR_LIST': ['z', 'y', 'x'],
         'VAR_DICT': {100: 99, 'abc': ['z', 'y', 'x']}
         }
    ),
]


@pytest.mark.parametrize("config_fpath, include_dunder_keys, assert_config_dict",
                         PYTHON_CONFIG_DICT_TEST_CASES
                         )
def test_config_dict_from_python_fpath(config_fpath, include_dunder_keys, assert_config_dict):
    # Load config dict
    test_config_dict = config_dict_from_python_fpath(
        config_fpath,
        include_dunder_keys=include_dunder_keys)

    # Remove special pytest keys added
    pytest_keys = ['@py_builtins', '@pytest_ar']
    for key in pytest_keys:
        if key in test_config_dict.keys():
            del test_config_dict[key]

    # Assert dictionaries are the same
    assert test_config_dict == assert_config_dict

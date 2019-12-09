# %%
import os
import shutil
from data_science_toolbox.io.get_absolute_fpath import get_absolute_fpath


def test_get_absolute_fpath():
    assert get_absolute_fpath() == os.path.abspath('.')

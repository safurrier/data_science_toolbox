# %%
import pandas as pd
import pytest
from data_science_toolbox.io.excel_to_df_dict import excel_to_df_dict

@pytest.mark.parametrize("data_path, correct_sheets",
                         [('tests/io/data/test_df_dict.xlsx', ['one', 'two', 'three'])])
def test_excel_to_df_dict(data_path, correct_sheets):
    test_df_dict = excel_to_df_dict(data_path)
    # Assert Dict[str, pd.DataFrame]
    assert isinstance(test_df_dict, dict)
    assert isinstance(list(test_df_dict.values())[0], pd.DataFrame)
    # Assert all sheets picked up
    assert list(test_df_dict.keys()) == correct_sheets


@pytest.mark.parametrize("data_path, include_sheets, correct_sheets",
                         [('tests/io/data/test_df_dict.xlsx',
                           ['one', 'three'],
                           ['one', 'three'])])
def test_excel_to_df_dict_include_sheets(data_path,
                                         include_sheets,
                                         correct_sheets):
    test_df_dict = excel_to_df_dict(
        data_path, include_sheets=include_sheets)
    # Assert Dict[str, pd.DataFrame]
    assert isinstance(test_df_dict, dict)
    assert isinstance(list(test_df_dict.values())[0], pd.DataFrame)
    # Assert included sheets picked up
    assert list(test_df_dict.keys()) == correct_sheets


@pytest.mark.parametrize("data_path, exclude_sheets, correct_sheets",
                         [('tests/io/data/test_df_dict.xlsx',
                           ['two'],
                           ['one', 'three'])])
def test_excel_to_df_dict_exclude_sheets(data_path,
                                         exclude_sheets,
                                         correct_sheets):
    test_df_dict = excel_to_df_dict(
        data_path, exclude_sheets=exclude_sheets)
    # Assert Dict[str, pd.DataFrame]
    assert isinstance(test_df_dict, dict)
    assert isinstance(list(test_df_dict.values())[0], pd.DataFrame)
    # Assert excluded sheets removed
    assert not [sheet_name for sheet_name
                in
                list(test_df_dict.keys())
                if sheet_name in exclude_sheets]


@pytest.mark.parametrize("data_path, include_sheets, exclude_sheets, correct_sheets",
                         [('tests/io/data/test_df_dict.xlsx',
                           ['one', 'three'],
                           ['three'],
                           ['one'])])
def test_excel_to_df_dict_include_and_exclude_sheets(data_path,
                                                     include_sheets,
                                                     exclude_sheets,
                                                     correct_sheets):
    test_df_dict = excel_to_df_dict(data_path,
                                    include_sheets=include_sheets,
                                    exclude_sheets=exclude_sheets)
    # Assert Dict[str, pd.DataFrame]
    assert isinstance(test_df_dict, dict)
    assert isinstance(list(test_df_dict.values())[0], pd.DataFrame)
    # Assert correct sheets. Included are included, excluded are excluded
    # With no intersection. Excluded column take precendence to
    # be removed even if in excluded columns
    assert list(test_df_dict.keys()) == correct_sheets

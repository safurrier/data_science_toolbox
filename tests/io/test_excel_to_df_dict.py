# %%
import pandas as pd
from data_science_toolbox.io.excel_to_df_dict import excel_to_df_dict

DATA_FPATH = 'tests/io/data/test_df_dict.xlsx'
TEST_ALL_SHEETS = ['one', 'two', 'three']
TEST_SHEETS_INCLUDE = ['one', 'three']
TEST_SHEETS_EXCLUDE = ['two']


def test_excel_to_df_dict():
    test_df_dict = excel_to_df_dict(DATA_FPATH)
    # Assert Dict[str, pd.DataFrame]
    assert isinstance(test_df_dict, dict)
    assert isinstance(list(test_df_dict.values())[0], pd.DataFrame)
    # Assert all sheets picked up
    assert list(test_df_dict.keys()) == TEST_ALL_SHEETS


def test_excel_to_df_dict_include_sheets():
    test_df_dict = excel_to_df_dict(
        DATA_FPATH, include_sheets=TEST_SHEETS_INCLUDE)
    # Assert Dict[str, pd.DataFrame]
    assert isinstance(test_df_dict, dict)
    assert isinstance(list(test_df_dict.values())[0], pd.DataFrame)
    # Assert included sheets picked up
    assert list(test_df_dict.keys()) == TEST_SHEETS_INCLUDE


def test_excel_to_df_dict_exclude_sheets():
    test_df_dict = excel_to_df_dict(
        DATA_FPATH, exclude_sheets=TEST_SHEETS_EXCLUDE)
    # Assert Dict[str, pd.DataFrame]
    assert isinstance(test_df_dict, dict)
    assert isinstance(list(test_df_dict.values())[0], pd.DataFrame)
    # Assert excluded sheets removed
    assert not [sheet_name for sheet_name
                in
                list(test_df_dict.keys())
                if sheet_name in TEST_SHEETS_EXCLUDE]


def test_excel_to_df_dict_include_and_exclude_sheets():
    test_df_dict = excel_to_df_dict(DATA_FPATH,
                                    include_sheets=TEST_SHEETS_INCLUDE,
                                    exclude_sheets=TEST_SHEETS_EXCLUDE)
    # Assert Dict[str, pd.DataFrame]
    assert isinstance(test_df_dict, dict)
    assert isinstance(list(test_df_dict.values())[0], pd.DataFrame)
    # Assert correct sheets. Included are included, excluded are excluded
    # With no intersection
    assert set(test_df_dict.keys()) == set(
        TEST_SHEETS_INCLUDE).difference(TEST_SHEETS_EXCLUDE)


test_excel_to_df_dict()
test_excel_to_df_dict_include_sheets()
test_excel_to_df_dict_exclude_sheets()
test_excel_to_df_dict_include_and_exclude_sheets()
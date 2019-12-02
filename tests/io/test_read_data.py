#%%
import pandas as pd
from data_science_toolbox.io.read_data import read_data

DATA_FPATH = 'tests/io/data/flag'
TEST_COLUMNS = ['name',	'landmass',	'zone']
TEST_READER_KWARGS = {'key':'data'}

def test_read_data_csv():
    test_df = read_data(DATA_FPATH+'.csv')
    # Make sure it's a dataframe
    assert isinstance(test_df, pd.DataFrame)
    # Make sure it has present rows
    assert test_df.shape[0] != 0

def test_read_data_excel():
    test_df = read_data(DATA_FPATH+'.xlsx')
    # Make sure it's a dataframe
    assert isinstance(test_df, pd.DataFrame)
    # Make sure it has present rows
    assert test_df.shape[0] != 0

def test_read_data_pickle():
    test_df = read_data(DATA_FPATH+'.pickle')
    # Make sure it's a dataframe
    assert isinstance(test_df, pd.DataFrame)
    # Make sure it has present rows
    assert test_df.shape[0] != 0

def test_read_data_pkl():
    test_df = read_data(DATA_FPATH+'.pkl')
    # Make sure it's a dataframe
    assert isinstance(test_df, pd.DataFrame)
    # Make sure it has present rows
    assert test_df.shape[0] != 0    

def test_read_data_hdf():
    test_df = read_data(DATA_FPATH+'.hdf', reader_kwargs=TEST_READER_KWARGS)
    # Make sure it's a dataframe
    assert isinstance(test_df, pd.DataFrame)
    # Make sure it has present rows
    assert test_df.shape[0] != 0

def test_read_data_reader_kwargs():
    test_df = read_data(DATA_FPATH+'.hdf', reader_kwargs=TEST_READER_KWARGS)
    # Make sure it's a dataframe
    assert isinstance(test_df, pd.DataFrame)
    # Make sure it has present rows
    assert test_df.shape[0] != 0

def test_read_data_column_subset():
    test_df = read_data(DATA_FPATH+'.csv', columns=TEST_COLUMNS)

    # Make sure it's a dataframe
    assert isinstance(test_df, pd.DataFrame)
    # Make sure it has present rows
    assert test_df.shape[0] != 0    
    # Assert same number of columns as selected
    assert test_df.shape[1] == len(TEST_COLUMNS)
    assert test_df.columns.values.tolist() == TEST_COLUMNS


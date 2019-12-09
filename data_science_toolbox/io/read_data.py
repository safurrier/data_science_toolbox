import pandas as pd
import pathlib
from typing import List


def read_data(fpath: str, columns: List[str] = None, reader_kwargs: dict = {}, ) -> pd.DataFrame:
    """
    Pass a filepath and have said file read in as a Pandas DataFrame.
    Supports csv, excel, hdf, pickle
    Parameters for reading in added as dict to reader_kwargs param


    Given a list of column names, check to see if each of those appears
    in the columns of a dataframe filtered by dtype=np.number

    Parameters
    ----------
    fpath : str
        A string filepath to the data file 
    columns : List[str]
        A list of columns to keep
    reader_kwargs : dict
        An optional dictionary of pandas reader kwargs

    Returns
    -------
    DataFrame
        A pandas DataFrame read in from the filepath

    Example
    -------

    hdf_kwargs = {
        'key': 'data'
    }
    df = read_data('my_hdf.hdf', reader_kwargs=hdf_kwargs)

    """

    # Check if extension in supported file format
    fpath = pathlib.Path(fpath)
    file_format = fpath.suffix
    if file_format not in ['.csv', '.pickle', '.pkl', '.xlsx', '.hdf']:
        print(
            f'File format "{file_format}" does not appear to be a supported file format')
        raise ValueError

    # Determine input file type and pandas reader
    if file_format == '.csv':
        reader = pd.read_csv
    elif (file_format == '.pickle') | (file_format == '.pkl'):
        reader = pd.read_pickle
    elif (file_format == '.xlsx'):
        reader = pd.read_excel
    elif (file_format == '.hdf'):
        reader = pd.read_hdf

    # Read in filepath:
    try:
        data = reader(fpath.as_posix(), **reader_kwargs)
    except FileNotFoundError as e:
        print(
            f'Unable to read in {fpath.as_posix()}. Check the file_format and file path')
        raise e

    missing_cols = []
    # If specificed, look for subset of columns
    if columns:
        columns = [col
                   if col in data.columns.values.tolist()
                   else missing_cols.append(col)
                   for col
                   in columns]
    else:
        columns = data.columns.values.tolist()

    assert columns != [None], 'No columns from columns param found in data'
    # Print missing columns if present
    if missing_cols:
        print(
            f'WARNING: These columns were not found in the data: {missing_cols}')

    # Subset to desired columns
    data = data[columns]

    return data

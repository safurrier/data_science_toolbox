import pandas as pd
import pathlib
from typing import Dict, List


def excel_to_df_dict(excel_path: str = None,
                     include_sheets: List[str] = None,
                     exclude_sheets: List[str] = None,
                     parse_kwds: dict = None) -> Dict[str, pd.DataFrame]:
    """Given a path to an excel file, read in the sheets to dataframes and return a dictionary
    of the form {sheet_name: dataframe}

    Parameters
    ----------
    excel_path : str
        A string filepath to the data file 
    include_sheets : List[str]
        A list of sheets to keep
    exclude_sheets : List[str]
        A list of sheets to exclude
    parse_kwds : dict
        An optional dictionary of pandas excel reader kwargs
    -------
    DataFrame
        A pandas DataFrame read in from the filepath

    Example
    -------

    df_dict = excel_to_df_dict('my_excel.xlsx', include_sheets=['sheet1', 'sheet2'])
    df_dict.keys()
    > ['sheet1', 'sheet2']
    """


    if not exclude_sheets:
        exclude_sheets = []
    if not parse_kwds:
        parse_kwds = {}
    excel_path = pathlib.Path(excel_path)

    # Read in Excel
    xl = pd.ExcelFile(excel_path.as_posix())
    # If no include sheets specified, keep all 
    if not include_sheets:
        include_sheets = list(xl.sheet_names)   
    # If specified load data in df_dict
    df_dict = {}
    for sheet_name in xl.sheet_names:
        # Filter down to exclusive set of sheets desired
        if sheet_name in include_sheets:
            # Parse data
            data = xl.parse(sheet_name, **parse_kwds)
            # Add to dictionary
            df_dict[sheet_name] = data
        if sheet_name in exclude_sheets:
            try:
                del df_dict[sheet_name]
            except KeyError:
                pass
    return df_dict 
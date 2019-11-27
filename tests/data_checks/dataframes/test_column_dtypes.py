import pandas as pd
import numpy as np
from data_science_toolbox.data_checks.dataframes.column_dtypes import are_numeric_columns


def test_are_numeric_columns():
    test_df = pd.DataFrame({
        'A': [1, 1, 1],
        'B': ['foo', 'bar', 'banana'],
        'C': [99.0, 23.5, 68.9]
    })
    assert all(are_numeric_columns(test_df, ['A', 'C']))

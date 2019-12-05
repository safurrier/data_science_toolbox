# coding: utf-8
import os
import warnings
import pandas as pd
import numpy as np
import click
import pathlib
from data_science_toolbox.io.get_absolute_fpath import get_absolute_fpath
from data_science_toolbox.io.python_config_dict import config_dict_from_python_fpath
from data_science_toolbox.io.read_data import read_data
from data_science_toolbox.io.export_data import export_data

# Silence C dtype mapping warnings
warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)
# Silence Deprecation Warning for click using importlib
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Change to root dir
os.chdir(get_absolute_fpath())

# Script Purpose
#################

# 1) Load in data from a source file and table (e.g. SQL, HDF, cloud etc)
# 2) Load in an sklearn pipeline for ETL transformation via the config file
# specified at --config_path which should be a python file holding necessary
# variables, specifically the ETL pipeline in variable PIPELINE
# 3) Export data to a db and table. If none is specified, use the import variable ones


@click.command()
@click.option('--config_path', default=None)
@click.option('--db_import_path', default=None)
@click.option('--db_input_table', default=None)
@click.option('--db_export_path', default=None)
@click.option('--db_export_table', default=None)
@click.option('--verbose', default=1)
def process_data(config_path: str = None,
                 db_import_path: str = None,
                 db_input_table: str = None,
                 db_export_path: str = None,
                 db_export_table: str = None,
                 verbose: int = None
                 ):
    """
    Process data script using click CLI with config file with Sklearn Pipeline.

    Supply an import path+table and config file with an sklearn pipeline to do ETL 
    and export the results


    Parameters
    ----------
    config_path : str
        A string filepath to a python config path. Must contain an
        sklearn Pipeline object under variable PIPELINE 
    db_import_path : search
        A string file path to the file/db connection string to the
        input data
    db_input_table : str, optional
        String table or key name if relevant
    db_export_path : search, optional
        A string file path/db connection string to export the 
        transformed data to
    db_export_table : str, optional
        String table or key name to export to if relevant
    verbose : int, optional
        An optional level of verbosity for CLI description of data 

    Return
    -------
    None

    Example
    -------

    > python process_data.py --config_path='src/config/etl_config.py' \
        --db_import_path='data/raw/01_raw_data.hdf' --db_input_table='data' \
        --db_export_path='data/interim/01_transformed_data.hdf' --db_export_table='data'

    """
    # Set export variables if none specified to be the same as import (e.g. inplace)
    if verbose:
        if (not db_export_path) | (not db_export_table):
            click.echo('No export variables set. Data ETL will be done in place at the'
                       f'db and table specified by db at "{db_export_path}" and table "{db_export_table}"')
    if not db_export_path:
        db_export_path = db_import_path
    if not db_export_table:
        db_export_table = db_input_table
    # Turn string paths into pathlib Paths
    db_import_path = pathlib.Path(db_import_path)
    db_export_path = pathlib.Path(db_export_path)
    # Read Config
    config = config_dict_from_python_fpath(config_path)

    # Read Data
    df = read_data(db_import_path.as_posix(),
                   reader_kwargs={'key': db_input_table})
    if verbose:
        click.echo(
            f'Reading in data from table {db_input_table} at {db_import_path.as_posix()}')
    # Process data with pipeline
    pipeline = config['PIPELINE']
    transformed_df = pipeline.fit_transform(df)
    # Write to DB
    if verbose:
        click.echo(
            f'Final datashape for transformed data is {transformed_df.shape}')
        click.echo(f'Compare to original shapes of: {df.shape}')
    if verbose:
        click.echo(
            f'Placing data into table "{db_export_table}" in the db at {db_export_path.as_posix()}')
    export_data(transformed_df, db_export_path.as_posix(),
                exporter_kwargs={'key': db_export_table})


if __name__ == '__main__':
    process_data()

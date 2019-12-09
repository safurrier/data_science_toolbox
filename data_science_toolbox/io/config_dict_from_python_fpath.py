import importlib
import pathlib


def config_dict_from_python_fpath(fpath: str = 'config.py', include_dunder_keys: bool = False) -> dict:
    """Use importlib and pathlib to take a string file path of a python config 
    file and return a dictionary of the config values for key:value. 

    By default the config dictionary removes default dunder methods of a python file.
    Location of fpath must be within a python module.

    Parameters
    ----------
    fpath : str
        String fpath of the python file to use as a config dict
    include_dunder_keys : bool = False
        Whether to include dunder values of file as config keys.
        Default is False (i.e. not included in config dict)

    Returns
    -------
    config_dict: dict
        A dictionary containing the variables set in the python
        file at 'fpath' as keys and values as respective values

    Example
    -------
    config = config_dict_from_python_fpath('config.py')
    > config
    > {'config_val_1':'A test string', config_val_2':1234}
    """
    # Turn string locaiton into path
    config_loc_path = pathlib.Path(fpath)

    # Get path as positive slash divided string
    # split it on '/' until the last part (the file)
    # Add the stem of the file name (remove extension)
    # Join on '.' so that it can be imported using importlib

    import_string = '.'.join(config_loc_path.as_posix().split(
        '/')[:-1]+[config_loc_path.stem])
    try:
        config_dict = importlib.import_module(import_string).__dict__
    except ModuleNotFoundError as e:
        print(
            f'Could not import file at "{config_loc_path.as_posix()}", are you sure this file exists here?')
        raise e

    if not include_dunder_keys:
        default_dunders = ['__name__', '__doc__', '__package__', '__loader__',
                           '__spec__', '__file__', '__cached__', '__builtins__']
        config_dict = {key: value for key,
                       value in config_dict.items() if key not in default_dunders}
    return config_dict

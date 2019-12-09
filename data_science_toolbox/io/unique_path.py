import pathlib
from typing import Union


def unique_path(directory: Union[str, pathlib.Path], name_pattern: str) -> pathlib.Path:
    """Given a pattern (e.g.f'test{:03d}.txt') and a directory return
    a pathlib.Path object with a unique file name

    Parameters
    ----------
    directory : Union[str, pathlib.Path]
        String or pathlib.Path used to check a directory
        create a unique fpath in
    name_pattern : int
        A formatted string with a pattern to assign an
        incremented digit name pattern (e.g.'test{:03d}.txt')
        Must be able to sucessfully format using string method:
        name_pattern.format(int)

    Returns
    -------
    unique_path: str
        The unique string fpath in the specified directory 

    Example
    -------

    Example Directory:
    + sample_dir
        + test_file_00.txt
        + test_file_01.txt

    > unique_fpath = unique_path('sample_dir', f'test_file_{:02d}.txt')
    > unique_fpath.as_posix()
    > 'sample_dir/test_file_02.txt'
    """
    # Turn directory into a pathlib.Path object
    # if not already one
    if not isinstance(directory, pathlib.Path):
        directory = pathlib.Path(directory)

    # Keep Track of increments
    counter = 0
    while True:
        counter += 1
        test_path = directory / name_pattern.format(counter)
        # If the file doesn't exist, return this path
        if not test_path.exists():
            unique_path = test_path
            break
    return unique_path

import os
import warnings


def get_absolute_fpath(target_fname: str = 'README.md', levels_to_check: int = 10, verbose: int = 0) -> str:
    """Pass a filename that exists in a directory an unknown number of
    levels higher. Return the string absolute path of said file.

    Parameters
    ----------
    target_fname : str, default = 'README.md'
        Filename to search for in parent directories.
        Default is a markdown file README
    levels_to_check : int
        The number of parent def
    verbose : int, optional
        An verbosity flag to print out the absolute fpath 
        found

    Returns
    -------
    target_dir: str
        The string absolute filepath to 'target_fname' 

    Example
    -------

    Example Directory:
    + sample_dir
        + target_file.txt
        + sub_sample_dir
            + sub_sub_sample_dir
            (current directory)

    target_fpath = get_absolute_fpath('target_file.txt')
    > target_fpath
    > C://users/projects/example_dir/sample_dir/target_file.txt
    """
    original_wd = os.getcwd()
    for x in range(0, levels_to_check):
        # If reached the max number of directory levels change to original wd and print message
        if x + 1 == levels_to_check:
            os.chdir(original_wd)
            if verbose:
                warnings.warn(
                    f"""\n\nUnable to find directory with file {target_fname} within {levels_to_check} parent directories""")
            target_dir = None
            break
        # Check if README exists
        elif os.path.isfile(target_fname):
            target_dir = os.getcwd()
            if verbose:
                print(f'Found target file in {target_dir}')
        # If not found move back one directory level
        else:
            os.chdir('../')
    return target_dir

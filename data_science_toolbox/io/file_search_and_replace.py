import os
import re
import pathlib

def file_search_and_replace(directory: str, search: str, replace: str, verbose: bool=True) -> None:
    """Given a directory, search all filenames in it for the regex pattern provided. 
    If found, replace with the provided string by renaming.
    By default, verbose=True prints message when file is renamed

    Parameters
    ----------
    directory : str
        A string filepath to the directory which will be searched 
    search : search
        A regex pattern to search filenames for
    replace : str
        String pattern to replace the match with
    verbose : bool
        An optional dictionary of pandas excel reader kwargs
    
    Return
    -------
    None

    Example
    -------

    Example Directory:
    + sample_dir
        + file_misssspelled1.txt
        + file_misspelled2.txt

    file_search_and_replace('sample_dir', 'missss', 'miss')
    
    > Renaming:
    > sample_dir/file_misssspelled1.txt
    > To:
    > sample_dir/file_misspelled1.txt)
    """    

    # Make path out of provided directory
    directory_path = pathlib.Path(directory)
    # Search directory filenames
    for filename in os.listdir(directory_path):
        # If there's a pattern match
        if re.search(search, filename):
            # Create a new filename replacing the old pattern
            new_fname = re.sub(search, replace, filename)
            # Rename it
            os.rename(directory_path / filename, directory_path / new_fname)
            # If verbose print the renamed files
            if verbose:
                print(f'Renaming:\n{directory_path / filename}\nTo:\n{directory_path / new_fname}\n\n')
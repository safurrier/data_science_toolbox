import pathlib


def directory_tree(directory: pathlib.Path) -> None:
    """Return a string that is a printable tree directory of the passed directory"""
    directory_tree_string = ''
    # Turn directory into a pathlib.Path object
    # if not already one
    if not isinstance(directory, pathlib.Path):
        directory = pathlib.Path(directory)
    #print(f'+ {directory}')
    directory_tree_string += f'\n+ {directory}'
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        #print(f'{spacer}+ {path.name}')
        directory_tree_string += f'\n{spacer}+ {path.name}'
    return directory_tree_string

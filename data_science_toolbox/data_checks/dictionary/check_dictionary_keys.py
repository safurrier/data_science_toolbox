from typing import Any, Dict, Generic, Iterable


def check_dictionary_keys(dictionary: Dict, required_keys: Iterable[Any], verbose: int = 0) -> bool:
    """
    Check a dictionary for keys given an iterable of keys to check

    Parameters
    ----------
    dictionary : dict
        The dictionary to check
    required_keys : Iterable
        An iterable of keys to check
    verbose : int
        Optional verbose setting. If non-zero, will print out missing keys        

    Returns
    -------
    Boolean
        Return True if all keys present in dictionary else False

    Example
    -------
    test_dict = {
        'A': [1, 1, 1],
        'B': ['foo', 'bar', 'banana'],
        'C': [99.0, 23.5, 68.9]
    }

    print(check_dictionary_keys(test_dict, ['A', 'C']))

    > True
    """
    missing_keys = []
    for key in required_keys:
        if key not in dictionary.keys():
            missing_keys.append(key)
    if missing_keys:
        if verbose > 0:
            print(
                f'Missing keys {missing_keys} not found in dictionary with keys {dictionary.keys()}')
        return False
    else:
        return True


def check_nested_dictionary_keys(dictionary: Dict, nested_keys_dict: Dict[Any, Iterable], verbose: int = 0) -> bool:
    """
    Check a dictionary for keys given an iterable of keys to check

    Parameters
    ----------
    dictionary : dict
        The dictionary to check
    required_keys : Iterable
        An iterable of keys to check
    verbose : int
        Optional verbose setting. If non-zero, will print out missing keys and nested keys     

    Returns
    -------
    Boolean
        Return True if all keys and nested keys present in dictionary else False

    Example
    -------
    test_dict = {
        'A': [1, 1, 1],
        'B': {'Nested_Key_1': 99.0, 'Nested_Key_2': 5, 'Nested_Key_3': 10},
        'C': {'Nested_Key_4': [99.0, 23.5, 68.9]}
    }

    print(check_nested_dictionary_keys(test_dict,
                                        {'B': ['Nested_Key_1', 'Nested_Key_2', 'Nested_Key_3'],
                                         'C': ['Nested_Key_4']})

    > True
    """
    missing_keys = []
    missing_nested_keys = []
    for key, nested_keys in nested_keys_dict.items():
        # Check that all top level keys are in the dictionary
        if key not in dictionary.keys():
            missing_keys.append(key)
        for nested_key in nested_keys:
            if nested_key not in dictionary[key].keys():
                missing_nested_keys.append(nested_key)
    if missing_keys:
        if verbose > 0:
            print(
                f'Missing keys {missing_keys} not found in dictionary with keys {dictionary.keys()}')
        return False
    if missing_nested_keys:
        if verbose > 0:
            print(
                f'Nested keys: {missing_nested_keys} not found in dictionary.')
        return False
    else:
        return True

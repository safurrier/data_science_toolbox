from data_science_toolbox.data_checks.dictionary.check_dictionary_keys import (
    check_dictionary_keys,
    check_nested_dictionary_keys,
)


def test_check_dictionary_keys():
    test_dict = {
        'A': [1, 1, 1],
        'B': ['foo', 'bar', 'banana'],
        'C': [99.0, 23.5, 68.9]
    }
    assert check_dictionary_keys(test_dict, ['A', 'C'])


def test_check_nested_dictionary_keys():

    test_dict = {
        'A': [1, 1, 1],
        'B': {'Nested_Key_1': 99.0, 'Nested_Key_2': 5, 'Nested_Key_3': 10},
        'C': {'Nested_Key_4': [99.0, 23.5, 68.9]}
    }
    assert check_nested_dictionary_keys(test_dict,
                                        {'B': ['Nested_Key_1', 'Nested_Key_2', 'Nested_Key_3'],
                                         'C': ['Nested_Key_4']})

"""
Implementations relative to ex 1.1 about unique characters in string
"""


def unique_chars(string):
    """
    Returns if all characters in string are unique
    Use an array to do so
    :param string:
    :return: if all characters in string are unique
    """
    array = [False] * 26
    for char in string:
        char_tab_index = ord(char.lower()) - 97
        if not array[char_tab_index]:
            array[char_tab_index] = True
        else:
            return False
    return True


def unique_chars_no_add_structure(string):
    """
    Returns if all characters in string are unique
    Use no additional structure
    :param string:
    :return: if all characters in string are unique
    """
    idx = 0
    while idx < len(string) - 1:
        if string[idx] in string[idx + 1:]:
            return False
        idx += 1
    return True

"""
Implementations relative to ex 1.3 about duplicates removal in string
"""


def remove_duplicates(array):
    """
    Returns unique elements in an array in natural order of apparition
    :param array: an array of elements
    :return: unique elements in array
    """
    str_length = len(array)
    if str_length < 2:
        return array
    tail = 1
    idx = 1
    while idx < str_length:
        if array[idx] not in array[:tail]:
            array[tail] = array[idx]
            tail += 1
        idx += 1
    return array[:tail]

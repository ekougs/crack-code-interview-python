"""
Implementations relative to ex 1.8 about string rotation detection
"""


def detect_string_rotation(str1, str2):
    """
    Test if the 2 strings are a rotation of one another
    :param str1: input
    :param str2: possible rotation
    :return: True if rotation false otherwise
    """
    return str2 in "{0}{0}".format(str1)

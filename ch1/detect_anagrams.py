"""
Implementations relative to ex 1.4 about anagrams
Other solution is to sort and compare the sorted strings O(n.log(n)
"""


def are_anagrams(str_1, str_2):
    """
    Detects if two words are anagram
    :param str_1: base string
    :param str_2: possible anagram
    :return: True if inputs are anagrams, False otherwise
    """
    if len(str_1) != len(str_2):
        return False
    letters_nb_1 = [0] * 256
    for char in str_1:
        letters_nb_1[ord(char.lower())] += 1

    for char in str_2:
        char_ord = ord(char.lower())
        if letters_nb_1[char_ord] > 0:
            letters_nb_1[char_ord] -= 1
        else:
            return False
    return letters_nb_1 == [0] * 256

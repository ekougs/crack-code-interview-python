"""
Implementation relative to ex 5.1 about setting a set of bits
"""


def set_bits(set_num, setting_num, start_idx, end_idx):
    """
    Number with bits set between provided position
    :param set_num: number that will be set
    :param setting_num: number to set
    :param start_idx: start index
    :param end_idx: end index
    :return: number with bits set between provided position
    """
    # last_idx - end_idx + 1 with last_idx = len - 1
    bit_length = _bit_length(set_num)
    num_of_1_on_the_left = bit_length - end_idx
    mask_first_part = ((2 ** num_of_1_on_the_left) - 1) << (bit_length - num_of_1_on_the_left)
    mask = mask_first_part | ((2 ** start_idx) - 1)
    return (mask & set_num) | (setting_num << start_idx)


def _bit_length(num):
    if num == 0 or num == 1:
        return 1
    bit_length = 0
    while num > 0:
        bit_length += 1
        num /= 2
    return bit_length

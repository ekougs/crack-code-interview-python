_decimal_separator = '.'


def decimal_binary_rep(decimal_str):
    if _decimal_separator in decimal_str:
        point_index = decimal_str.index(_decimal_separator)
    else:
        point_index = len(decimal_str)
    int_part = _integer_binary_str(int(decimal_str[:point_index]))
    # Decimal part should have less than 32 char
    binary_str = int_part
    decimal_part_str = ''
    if point_index < len(decimal_str):
        decimal_part_str += _decimal_separator
        decimal_part = float(decimal_str[point_index:])
        # binary part is equal to sum for i from 0 to n of Ci * 2 ^ -i
        # to find Ci, you multiply the base 10 decimal part by 2
        # if the product is >= 1 then Ci = 0 and we go on with the product minus 1
        # otherwise Ci = 0 and we go on with the product
        # and iterate until decimal part = 0 or the floating point limit is reached
        while decimal_part > 0:
            if len(decimal_part_str) == 32:
                raise FloatingPointError
            if decimal_part == 1:
                decimal_part_str += '1'
                break
            decimal_part_shift = decimal_part * 2
            if decimal_part_shift >= 1:
                decimal_part_str += '1'
                decimal_part = decimal_part_shift - 1
            else:
                decimal_part_str += '0'
                decimal_part = decimal_part_shift
    return binary_str + decimal_part_str


def _integer_binary_str(decimal, limit=None):
    binary_str = ''
    binary_str_length = 0
    while decimal != 0:
        binary_str += (str(decimal % 2))
        binary_str_length += 1
        if limit and binary_str_length > limit:
            raise FloatingPointError
        decimal >>= 1
    return binary_str

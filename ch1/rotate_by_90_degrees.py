"""
Implementations relative to ex 1.5 about 90 degrees rotation
"""


def rotate_by_90_degrees(square_image_int_arr):
    """
    Rotate in place all elements by 90 degrees
    :param square_image_int_arr: square int matrix
    :return: rotated square int matrix input
    """
    dimension = len(square_image_int_arr[0])
    left_top_most = __find_most_inner_square_left_top_most_point(square_image_int_arr)
    if dimension % 2 == 0:
        inner_dimension = 2
    else:
        inner_dimension = 3
    __rotate_all_inner_squares(inner_dimension, left_top_most, square_image_int_arr)
    return square_image_int_arr


def __find_most_inner_square_left_top_most_point(square_image_int_arr):
    dimension = len(square_image_int_arr)
    return dimension / 2 - 1


def __rotate_all_inner_squares(inner_dimension, min_col_line_idx, square_image_int_arr):
    while min_col_line_idx >= 0:
        max_col_line_idx = min_col_line_idx + inner_dimension - 1

        __rotate_inner_square(min_col_line_idx, max_col_line_idx, square_image_int_arr)

        min_col_line_idx -= 1
        inner_dimension += 2


def __rotate_inner_square(min_col_line_idx, max_col_line_idx, square_image_int_arr):
    i = 0
    while i < max_col_line_idx - min_col_line_idx:
        # Rotate the 4 elements at the same and just use one element buffer
        element_buffer = square_image_int_arr[min_col_line_idx + i][max_col_line_idx]
        square_image_int_arr[min_col_line_idx + i][max_col_line_idx] = \
            square_image_int_arr[min_col_line_idx][min_col_line_idx + i]
        square_image_int_arr[min_col_line_idx][min_col_line_idx + i] = element_buffer

        element_buffer = square_image_int_arr[max_col_line_idx][max_col_line_idx - i]
        square_image_int_arr[max_col_line_idx][max_col_line_idx - i] = \
            square_image_int_arr[min_col_line_idx][min_col_line_idx + i]
        square_image_int_arr[min_col_line_idx][min_col_line_idx + i] = element_buffer

        element_buffer = square_image_int_arr[max_col_line_idx - i][min_col_line_idx]
        square_image_int_arr[max_col_line_idx - i][min_col_line_idx] = \
            square_image_int_arr[min_col_line_idx][min_col_line_idx + i]
        square_image_int_arr[min_col_line_idx][min_col_line_idx + i] = element_buffer
        i += 1

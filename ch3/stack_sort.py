"""
Implementation relative to ex 3.6 about sort algorithm for stack
"""
from ch3.stack_struct import Stack


def insertion_sort_stack(stack):
    """
    Sort input in ascending order
    :param stack: stack to sort
    :return: sorted stack
    """
    sorted_stack = Stack(stack.pop())

    while not stack.is_empty():
        elt_to_insert = stack.pop()
        # Stack first elements will be in reverse order
        while not sorted_stack.is_empty() and sorted_stack.peek().value < elt_to_insert:
            stack.push(sorted_stack.pop())
        sorted_stack.push(elt_to_insert)

    return sorted_stack


def __insert_as_min__(stack, elt):
    min_elt = stack.peek().value
    print elt, min_elt
    if elt <= min_elt:
        stack.push(elt)
        return True
    return False

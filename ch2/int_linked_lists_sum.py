"""
Implementations relative to ex 2.4 about sum using linked lists
"""
from structure.linked_list import LinkedList


def sum_linked_lists(l1, l2):
    """
    Sums the 2 provided number and return the linked list representation of the sum
    :param l1: first number digits in reverse order
    :param l2: second number digits in reverse order
    :return:
    """
    linked_list = None
    n1 = l1.root
    n2 = l2.root
    rest = 0

    while n1 is not None or n2 is not None:
        digit_sum = 0
        if n1 is None:
            digit_sum = n2.value + rest
        elif n2 is None:
            digit_sum = n1.value + rest
        else:
            digit_sum = (n1.value + n2.value + rest)

        int_sum = int(digit_sum % 10)
        rest = int(digit_sum / 10)
        if linked_list is None:
            linked_list = LinkedList(int_sum)
        else:
            linked_list.push(int_sum)

        if n1 is not None:
            n1 = n1.next_node
        if n2 is not None:
            n2 = n2.next_node

    if rest != 0:
        linked_list.push(rest)

    return linked_list

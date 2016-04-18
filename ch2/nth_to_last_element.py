"""
Implementations relative to ex 2.2 about nth to last element in a linked list
"""


def nth_to_last_element(linked_list, n):
    """
    :param linked_list: linked list to browse
    :param n: the nth to last we want to retrieve
    :return: nth to last element value
    """
    idx = 0
    p1 = linked_list.root
    for _ in linked_list:
        if idx > n:
            p1 = p1.next_node
        idx += 1
    return p1.value

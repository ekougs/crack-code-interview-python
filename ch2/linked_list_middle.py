"""
Implementations relative to ex 2.3 about middle of a linked list
"""


def middle(linked_list):
    """
    Return the element value in the middle for a linked list
    :param linked_list: input
    :return: element value in the middle
    """
    two_by_two_pointer = linked_list.root
    for node in linked_list:
        if two_by_two_pointer == linked_list.root:
            two_by_two_pointer = two_by_two_pointer.next_node
        else:
            two_by_two_pointer = two_by_two_pointer.next_node.next_node
        if two_by_two_pointer is None or two_by_two_pointer.next_node is None:
            return node.value

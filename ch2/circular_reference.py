"""
Implementations relative to ex 2.5 about circular reference in linked lists
"""


def circular_reference(linked_list):
    """
    Return element that cause circular reference
    :param linked_list: list to check
    :return: element that cause circular reference
    """
    two_by_two_pointer = linked_list.root
    for node in linked_list:
        if two_by_two_pointer == linked_list.root:
            two_by_two_pointer = two_by_two_pointer.next_node
        else:
            two_by_two_pointer = two_by_two_pointer.next_node.next_node
        if two_by_two_pointer is None or two_by_two_pointer.next_node is None:
            return None
        if node == two_by_two_pointer:
            return node

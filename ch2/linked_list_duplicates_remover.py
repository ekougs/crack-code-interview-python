"""
Implementations relative to ex 2.1 about removal in a linked list
"""


def remove_duplicates(linked_list):
    """
    Removes duplicates in a linked list
    :param linked_list: a linked list
    :return: linked list with unique elements
    """
    unique_elements = []
    previous_node = None
    for current_node in linked_list:
        if previous_node is not None and current_node.value not in unique_elements:
            previous_node.next_node = current_node.next_node
        else:
            unique_elements.append(current_node.next_node)
        previous_node = current_node
    return linked_list


def remove_duplicates_no_buff(linked_list):
    """
    Removes duplicates in a linked list with no additional buffer
    :param linked_list: a linked list
    :return: linked list with unique elements
    """

    def not_in_list(node):
        cur_node = linked_list.root
        while cur_node != node:
            if cur_node.value == node.value:
                return True
            cur_node = cur_node.next_node
        return False

    previous_node = None
    for current_node in linked_list:
        if previous_node is not None and not_in_list(current_node):
            previous_node.next_node = current_node.next_node
        previous_node = current_node

    return linked_list

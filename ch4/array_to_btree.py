from ch3.stack_struct import Stack
from structure.binary_tree import BinaryTree, BinaryTreeNode

"""
Implementation relative to ex 4.3 about creating a balanced btree from a sorted array
"""


def _insert_node(btree, value, parent):
    if parent is None:
        return btree.insert(value)
    elif value < parent.value:
        node = BinaryTreeNode(value=value)
        parent.left = node
    else:
        node = BinaryTreeNode(value=value)
        parent.right = node
    return node


def to_btree(sorted_list):
    """
    Turns a list into a btree. if list is sorted, btree will be balanced
    :param sorted_list: sorted list
    :return: balanced btree if array is sorted. btree is not balanced if array is not sorted
    """
    middle_idx = int(len(sorted_list) / 2)
    idx_parent_tuples = Stack((middle_idx, None))
    marked = []
    btree = BinaryTree()
    parent = None
    while not idx_parent_tuples.is_empty():
        idx_parent_tuple = idx_parent_tuples.pop()
        idx = idx_parent_tuple[0]
        marked.append(idx)
        value = sorted_list[idx]
        node = _insert_node(btree, value, parent)
        if idx - 1 >= 0 and idx - 1 not in marked:
            idx_parent_tuples.push(((idx - 1), node))
        if idx + 1 < len(sorted_list) and idx + 1 not in marked:
            idx_parent_tuples.push(((idx + 1), node))
    return btree

from structure.binary_tree import BinaryTree

"""
Implementation relative to ex 4.1 about balanced binary tree
"""


def is_balanced_tree(tree):
    """
    Determine if tree is balanced
    :param tree: simple binary tree
    :return: if tree is balanced
    """
    root = tree.root
    diff = abs(_size(root.left) - _size(root.right))
    return diff <= 1


def _size(node):
    if node is BinaryTree.EMPTY_NODE:
        return 0
    return max(_size(node.left), _size(node.right)) + 1

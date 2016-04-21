"""
Implementation relative to ex 4.7 about big trees and subtrees, fails fast algorithm
"""
from ch3.stack_struct import Stack


def is_subtree(tree, subtree):
    """
    :param tree: the containing tree
    :param subtree: the contained tree
    :return: True if subtree is contained by tree, False otherwise
    """
    subtree_node = subtree.root
    subtree_value = subtree_node.value
    if not tree.contains(subtree_value):
        return False
    tree_node = tree.get(subtree_value)
    corresponding_nodes_stack = Stack((subtree_node, tree_node))
    while not corresponding_nodes_stack.is_empty():
        corresponding_nodes = corresponding_nodes_stack.pop()
        subtree_node = corresponding_nodes[0]
        tree_node = corresponding_nodes[1]
        if subtree_node.value != tree_node.value:
            return False
        if not subtree_node.left_empty():
            corresponding_nodes_stack.push((subtree_node.left, tree_node.left))
        if not subtree_node.right_empty():
            corresponding_nodes_stack.push((subtree_node.right, tree_node.right))
    return True

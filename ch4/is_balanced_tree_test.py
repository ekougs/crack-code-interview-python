from unittest import TestCase

from ch4.is_balanced_tree import is_balanced_tree
from structure.binary_tree import BinaryTree


class IsBalancedTreeTest(TestCase):
    def test_should_detect_tree_is_balanced_for_same_branches_size(self):
        tree = BinaryTree()
        tree.insert(3)
        tree.insert(1)
        tree.insert(2)
        tree.insert(4)
        tree.insert(5)
        self.assertTrue(is_balanced_tree(tree))

    def test_should_detect_tree_is_balanced_for_diff_1_in_branches_size(self):
        tree = BinaryTree()
        tree.insert(3)
        tree.insert(1)
        tree.insert(2)
        tree.insert(4)
        tree.insert(5)
        tree.insert(6)
        self.assertTrue(is_balanced_tree(tree))

    def test_should_detect_tree_is_unbalanced(self):
        tree = BinaryTree()
        tree.insert(3)
        tree.insert(1)
        tree.insert(2)
        tree.insert(4)
        tree.insert(5)
        tree.insert(6)
        tree.insert(7)
        self.assertFalse(is_balanced_tree(tree))

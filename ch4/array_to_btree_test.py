from unittest import TestCase

from ch4.array_to_btree import to_btree
from ch4.is_balanced_tree import is_balanced_tree


class ArrayToBTreeTest(TestCase):
    def test_should_create_a_balanced_btree_for_sorted_array(self):
        btree = to_btree([1, 2, 3, 4, 5, 6])
        self.assertTrue(is_balanced_tree(btree))

    def test_should_create_a_balanced_btree_for_sorted_array_with_non_unique_elements(self):
        btree = to_btree([1, 2, 3, 4, 4, 5, 6, 7])
        self.assertTrue(is_balanced_tree(btree))

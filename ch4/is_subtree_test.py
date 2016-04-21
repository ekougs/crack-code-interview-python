from unittest import TestCase

from ch4.array_to_btree import to_btree
from ch4.is_subtree import is_subtree


class IsSubtreeTest(TestCase):
    def test_should_be_subtree(self):
        container = to_btree([1, 2, 3, 4, 5, 6])
        contained = to_btree([1, 3, 2])
        self.assertTrue(is_subtree(container, contained))

    def test_should_not_be_subtree(self):
        container = to_btree([1, 2, 3, 4, 5, 6])
        contained = to_btree([2, 3, 4])
        self.assertFalse(is_subtree(container, contained))

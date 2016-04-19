from unittest import TestCase

from structure.binary_tree import BinaryTree


class BinaryTreeTest(TestCase):
    subject = BinaryTree()
    subject.insert(3)
    subject.insert(1)
    subject.insert(2)
    subject.insert(4)
    subject.insert(5)
    subject.insert(6)
    subject.insert(7)

    def test_should_return_size_5_for_created_tree(self):
        self.assertEqual(5, self.subject.size())

    def test_should_return_true_for_contains_6_query(self):
        self.assertTrue(self.subject.contains(6))

    def test_should_return_false_for_contains_8_query(self):
        self.assertFalse(self.subject.contains(8))

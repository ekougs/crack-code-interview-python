from unittest import TestCase

from ch2.linked_list_middle import middle
from structure.linked_list import LinkedList


class LinkedListMiddleTest(TestCase):
    def test_should_return_4_for_1_2_3_4_5_6_7(self):
        linked_list = LinkedList(1).push(2).push(3).push(4).push(5).push(6).push(7)
        self.assertEqual(4, middle(linked_list))

    def test_should_return_3_for_1_2_3_4_5_6(self):
        linked_list = LinkedList(1).push(2).push(3).push(4).push(5).push(6)
        self.assertEqual(3, middle(linked_list))

    def test_should_return_1_for_1_2(self):
        linked_list = LinkedList(1).push(2)
        self.assertEqual(1, middle(linked_list))

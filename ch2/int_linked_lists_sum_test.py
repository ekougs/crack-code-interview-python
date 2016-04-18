from unittest import TestCase

from ch2.int_linked_lists_sum import sum_linked_lists
from structure.linked_list import LinkedList


class LinkedListSumTest(TestCase):
    def test_should_return_8_0_8_for_3_1_5_plus_5_9_2(self):
        l1 = LinkedList(3).push(1).push(5)
        l2 = LinkedList(5).push(9).push(2)
        self.assertEqual("8 -> 0 -> 8", str(sum_linked_lists(l1, l2)))

    def test_should_return_8_0_0_1_for_3_1_7_plus_5_9_2(self):
        l1 = LinkedList(3).push(1).push(7)
        l2 = LinkedList(5).push(9).push(2)
        self.assertEqual("8 -> 0 -> 0 -> 1", str(sum_linked_lists(l1, l2)))

    def test_should_return_8_0_3_for_3_1_plus_5_9_2(self):
        l1 = LinkedList(3).push(1)
        l2 = LinkedList(5).push(9).push(2)
        self.assertEqual("8 -> 0 -> 3", str(sum_linked_lists(l1, l2)))

    def test_should_return_8_0_3_for_5_9_2_1_plus_3_1(self):
        l1 = LinkedList(5).push(9).push(2).push(1)
        l2 = LinkedList(3).push(1)
        self.assertEqual("8 -> 0 -> 3 -> 1", str(sum_linked_lists(l1, l2)))

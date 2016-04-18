from unittest import TestCase

from ch2.nth_to_last_element import nth_to_last_element
from structure.linked_list import LinkedList


class NthToLastTest(TestCase):
    def test_should_find_1_for_3_1_2_list_and_1(self):
        linked_list = LinkedList(3).push(1).push(2)
        self.assertEqual(1, nth_to_last_element(linked_list, 1))

    def test_should_find_2_for_3_1_2_4_5_list_and_2(self):
        linked_list = LinkedList(3).push(1).push(2).push(4).push(5)
        self.assertEqual(2, nth_to_last_element(linked_list, 2))

from unittest import TestCase

from ch2.linked_list_duplicates_remover import remove_duplicates, remove_duplicates_no_buff
from structure.linked_list import LinkedList


class RemoveDuplicatesTest(TestCase):
    def test_should_return_1_2_3_for_1_1_2_2_3_3(self):
        linked_list = LinkedList(1).push(1).push(2).push(2).push(3).push(3)
        linked_list = remove_duplicates(linked_list)
        self.assertEqual(str(linked_list), str(LinkedList(1).push(2).push(3)))

    def test_should_return_1_2_3_for_1_1_2_2_3_3_no_buff(self):
        linked_list = LinkedList(1).push(1).push(2).push(2).push(3).push(3)
        linked_list = remove_duplicates_no_buff(linked_list)
        self.assertEqual(str(linked_list), str(LinkedList(1).push(2).push(3)))

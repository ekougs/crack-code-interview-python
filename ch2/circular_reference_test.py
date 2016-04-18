from unittest import TestCase

from ch2.circular_reference import circular_reference
from structure.linked_list import LinkedList


class CircularReferenceTest(TestCase):
    def test_should_detect_C_as_circular_ref_in_A_B_C_D_E_C(self):
        linked_list = LinkedList('A').push('B').push('C')
        c = linked_list.last
        linked_list.push('D').push('E')
        linked_list.last.next_node = c
        self.assertEqual(c, circular_reference(linked_list))

    def test_should_detect_no_circular_ref_in_A_B_C_D_E(self):
        linked_list = LinkedList('A').push('B').push('C').push('D').push('E')
        self.assertTrue(circular_reference(linked_list) is None)

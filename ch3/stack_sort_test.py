from unittest import TestCase

from ch3.stack_sort import insertion_sort_stack
from ch3.stack_struct import Stack


class SortStackTest(TestCase):
    def test_should_sort_S_E_N_N_E_N_to_E_E_N_N_N_S(self):
        stack = Stack("S").push("E").push("N").push("N").push("E").push("N")
        self.assertEqual("E -> E -> N -> N -> N -> S", str(insertion_sort_stack(stack)))

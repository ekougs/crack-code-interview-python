from unittest import TestCase

from ch3.stack_struct import Stack


class StackTest(TestCase):
    def test_should_be_able_to_find_min(self):
        stack = Stack(3).push(5).push(2).push(1).push(8).push(4)
        self.assertEqual(1, stack.min())

    def test_should_be_able_to_find_second_min_after_pop_of_min(self):
        stack = Stack(3).push(5).push(2).push(8).push(4).push(1)
        stack.pop()
        self.assertEqual(2, stack.min())

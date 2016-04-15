from unittest import TestCase

from ch1 import remove_duplicate_chars


class RemoveDuplicateTest(TestCase):
    def test_should_return_a_for_remove_duplicate_a(self):
        a_arr = list("a")
        self.assertEqual(a_arr, remove_duplicate_chars.remove_duplicates(a_arr))

    def test_should_return_first_for_remove_duplicate_first(self):
        first_arr = list("first")
        self.assertEqual(first_arr, remove_duplicate_chars.remove_duplicates(first_arr))

    def test_should_return_apriton_for_remove_duplicate_apparition(self):
        self.assertEqual(list("apriton"), remove_duplicate_chars.remove_duplicates(list("apparition")))

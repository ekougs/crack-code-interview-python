from unittest import TestCase

from ch1 import unique_chars


class UniqueCharsTest(TestCase):
    def test_should_return_true_for_abcdefg(self):
        self.assertTrue(unique_chars.unique_chars("abcdefg"))

    def test_should_return_false_for_abcdefa(self):
        self.assertFalse(unique_chars.unique_chars("abcdefa"))

    def test_no_add_should_return_true_for_abcdefg(self):
        self.assertTrue(unique_chars.unique_chars_no_add_structure("abcdefg"))

    def test_no_add_should_return_false_for_abcdefa(self):
        self.assertFalse(unique_chars.unique_chars_no_add_structure("abcdefa"))

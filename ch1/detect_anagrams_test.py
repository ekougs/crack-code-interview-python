from unittest import TestCase

from ch1 import detect_anagrams


class RemoveDuplicateTest(TestCase):
    def test_should_detect_anagram_for_elvis_lives(self):
        self.assertTrue(detect_anagrams.are_anagrams("elvis", "lives"))

    def test_should_not_detect_anagram_for_elise_lives(self):
        self.assertFalse(detect_anagrams.are_anagrams("elise", "lives"))

    def test_should_not_detect_anagram_for_elsa_lives(self):
        self.assertFalse(detect_anagrams.are_anagrams("elsa", "lives"))

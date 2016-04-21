from unittest import TestCase

from ch5.bit_setter import set_bits


class BitSetterTest(TestCase):
    def test_should_return_10001010100_for_10000000000_10101_2_6(self):
        actual = set_bits(0b10000000000, 0b10101, 2, 6)
        self.assertEqual(0b10001010100, actual)

    def test_should_return_10001010100_for_10001111100_10101_2_6(self):
        actual = set_bits(0b10001111100, 0b10101, 2, 6)
        self.assertEqual(0b10001010100, actual)

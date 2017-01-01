from unittest import TestCase

from ch5.decimal_binary_representation import decimal_binary_rep


class DecimalBinaryRepresentationTest(TestCase):
    def test_should_return_11_for_3(self):
        # GIVEN
        decimal = '3'
        # WHEN
        actual = decimal_binary_rep(decimal)
        # THEN
        self.assertEqual('11', actual)

    def test_should_return_11_1_for_3_5(self):
        # GIVEN
        decimal = '5.125'
        # WHEN
        actual = decimal_binary_rep(decimal)
        # THEN
        self.assertEqual('101.001', actual)

    def test_should_raise_error_for_3_3(self):
        # GIVEN
        decimal = '3.3'
        # WHEN
        self.assertRaises(FloatingPointError, decimal_binary_rep, decimal)
        # THEN
        # Raises FloatingPointError

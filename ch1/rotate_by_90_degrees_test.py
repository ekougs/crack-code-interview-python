from unittest import TestCase

from ch1 import rotate_by_90_degrees


class Rotate90DegreesTest(TestCase):
    def test_should_rotate_2_dimensional_square_arr(self):
        actual = rotate_by_90_degrees.rotate_by_90_degrees([[1, 2],
                                                            [3, 4]])
        self.assertEqual(actual, [[3, 1],
                                  [4, 2]])

    def test_should_rotate_3_dimensional_square_arr(self):
        actual = rotate_by_90_degrees.rotate_by_90_degrees([[1, 2, 3],
                                                            [4, 5, 6],
                                                            [7, 8, 9]])
        self.assertEqual(actual, [[7, 4, 1],
                                  [8, 5, 2],
                                  [9, 6, 3]])

    def test_should_rotate_4_dimensional_square_arr(self):
        actual = rotate_by_90_degrees.rotate_by_90_degrees([[1, 2, 3, 4],
                                                            [1, 2, 3, 4],
                                                            [1, 2, 3, 4],
                                                            [1, 2, 3, 4]])
        self.assertEqual(actual, [[1, 1, 1, 1],
                                  [2, 2, 2, 2],
                                  [3, 3, 3, 3],
                                  [4, 4, 4, 4]])

    def test_should_rotate_5_dimensional_square_arr(self):
        actual = rotate_by_90_degrees.rotate_by_90_degrees([[1, 2, 3, 4, 5],
                                                            [1, 2, 3, 4, 5],
                                                            [1, 2, 3, 4, 5],
                                                            [1, 2, 3, 4, 5]])
        self.assertEqual(actual, [[1, 1, 1, 1, 1],
                                  [2, 2, 2, 2, 2],
                                  [3, 3, 3, 3, 3],
                                  [4, 4, 4, 4, 4],
                                  [5, 5, 5, 5, 5]])

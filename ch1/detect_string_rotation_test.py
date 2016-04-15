from unittest import TestCase

from ch1 import detect_string_rotation


class DetectStringRotationTest(TestCase):
    def test_should_detect_erbottlewat_is_rotation_of_waterbottle(self):
        self.assertTrue(detect_string_rotation.detect_string_rotation("erbottlewat", "waterbottle"))

    def test_should_detect_elisa_is_not_rotation_of_elsa(self):
        self.assertFalse(detect_string_rotation.detect_string_rotation("elisa", "elsa"))

import unittest

from src.fcops.floris_modes import get_floris_mode_label


class TestFlorisModes(unittest.TestCase):
    def test_get_floris_mode_label_valid(self):
        self.assertEqual(get_floris_mode_label(0), "OBS___")
        self.assertEqual(get_floris_mode_label(1), "DARKNP")
        self.assertEqual(get_floris_mode_label(11), "DARKSR")
        self.assertEqual(get_floris_mode_label(20), "DEFRTS")
        self.assertEqual(get_floris_mode_label(21), "DEFDAR")
        self.assertEqual(get_floris_mode_label(25), "DARKOC")
        self.assertEqual(get_floris_mode_label(31), "DRKMTF")
        self.assertEqual(get_floris_mode_label(32), "DARKSTR")
        self.assertEqual(get_floris_mode_label(51), "SUN___")
        self.assertEqual(get_floris_mode_label(52), "DEFSUN")
        self.assertEqual(get_floris_mode_label(53), "MOON__")
        self.assertEqual(get_floris_mode_label(54), "CLOUD_")
        self.assertEqual(get_floris_mode_label(61), "MOONSL")
        self.assertEqual(get_floris_mode_label(71), "LINDES")
        self.assertEqual(get_floris_mode_label(72), "LINSEA")
        self.assertEqual(get_floris_mode_label(73), "LINSUN")
        self.assertEqual(get_floris_mode_label(74), "LINDAR")
        self.assertEqual(get_floris_mode_label(81), "CTE___")

    def test_get_floris_mode_label_string(self):
        self.assertEqual(get_floris_mode_label("1"), "DARKNP")
        self.assertEqual(get_floris_mode_label("81"), "CTE___")

    def test_get_floris_mode_label_invalid(self):
        with self.assertRaises(ValueError):
            get_floris_mode_label(999)

    def test_get_floris_mode_label_non_integer(self):
        with self.assertRaises(ValueError):
            get_floris_mode_label("not-a-number")

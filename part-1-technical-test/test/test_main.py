import unittest

from src.main import stamp_duty_calculator


class StampDutyCalculatorTests(unittest.TestCase):

    def test_invalid_input(self):
        with self.assertRaisesRegex(ValueError, "property_price must be a number"):
            stamp_duty_calculator(None)

    def test_bool_rejected(self):
        with self.assertRaisesRegex(ValueError, "property_price must be a number"):
            stamp_duty_calculator(True)

    def test_non_finite_rejected(self):
        for value in (float("nan"), float("inf")):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "property_price must be a finite number"):
                    stamp_duty_calculator(value)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "property_price must be a positive number"):
            stamp_duty_calculator(-100_000)

    def test_zero(self):
        self.assertEqual(stamp_duty_calculator(0), 0)

    def test_first_band(self):
        self.assertEqual(stamp_duty_calculator(125_000), 0)

    def test_just_above_first_threshold(self):
        self.assertAlmostEqual(stamp_duty_calculator(125_001), 0.05)

    def test_middle_band(self):
        self.assertEqual(stamp_duty_calculator(500_000), 18_750)

    def test_second_threshold(self):
        self.assertEqual(stamp_duty_calculator(725_000), 30_000)

    def test_just_above_second_threshold(self):
        self.assertAlmostEqual(stamp_duty_calculator(725_001), 30_000.15)

    def test_top_band(self):
        self.assertEqual(stamp_duty_calculator(1_000_000), 71_250)


if __name__ == "__main__":
    unittest.main()

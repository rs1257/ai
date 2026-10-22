import unittest

from src.main import stamp_duty_calculator


class StampDutyCalculatorTests(unittest.TestCase):

    def test_invalid_input(self):
        with self.assertRaisesRegex(ValueError, "property_price must be a number"):
            stamp_duty_calculator(None)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "property_price must be a positive number"):
            stamp_duty_calculator(-100_000)

    def test_zero(self):
        self.assertEqual(stamp_duty_calculator(0), 0)

    def test_first_band(self):
        self.assertEqual(stamp_duty_calculator(125_000), 0)

    def test_middle_band(self):
        self.assertEqual(stamp_duty_calculator(500_000), 18_750)

    def test_top_band(self):
        self.assertEqual(stamp_duty_calculator(1_000_000), 71_250)


if __name__ == "__main__":
    unittest.main()

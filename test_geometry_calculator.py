import unittest

from main import GeometryCalculator


class TestGeometryCalculator(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(GeometryCalculator.circle_area(5), 78.54, places=2)
        self.assertRaises(ValueError, GeometryCalculator.circle_area, -5)

    def test_triangle_area(self):
        self.assertAlmostEqual(GeometryCalculator.triangle_area(3, 4, 5), 6.0, places=2)
        self.assertAlmostEqual(
            GeometryCalculator.triangle_area(7, 8, 9), 26.83, places=2
        )
        self.assertRaises(ValueError, GeometryCalculator.triangle_area, 0, 4, 5)
        self.assertRaises(ValueError, GeometryCalculator.triangle_area, 3, -4, 5)

    def test_rectangle_area(self):
        self.assertAlmostEqual(GeometryCalculator.rectangle_area(4, 6), 24.0, places=2)
        self.assertRaises(ValueError, GeometryCalculator.rectangle_area, -4, 6)

    def test_square_area(self):
        self.assertAlmostEqual(GeometryCalculator.square_area(4), 16.0, places=2)
        self.assertRaises(ValueError, GeometryCalculator.square_area, -4)

    def test_is_right_triangle(self):
        self.assertTrue(GeometryCalculator.is_right_triangle(3, 4, 5))
        self.assertTrue(GeometryCalculator.is_right_triangle(5, 12, 13))
        self.assertTrue(GeometryCalculator.is_right_triangle(8, 15, 17))
        self.assertFalse(GeometryCalculator.is_right_triangle(3, 4, 6))
        self.assertRaises(ValueError, GeometryCalculator.triangle_area, 1, 2, 15)

    def test_calculate_area(self):
        self.assertAlmostEqual(
            GeometryCalculator.calculate_area(radius=5), 78.54, places=2
        )
        self.assertAlmostEqual(
            GeometryCalculator.calculate_area(side1=3, side2=4, side3=5), 6.0, places=2
        )
        self.assertAlmostEqual(
            GeometryCalculator.calculate_area(side1=4, side2=6), 24.0, places=2
        )
        self.assertAlmostEqual(
            GeometryCalculator.calculate_area(side=4), 16.0, places=2
        )
        self.assertRaises(ValueError, GeometryCalculator.calculate_area, radius=-5)


if __name__ == "__main__":
    unittest.main()

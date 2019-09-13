from unittest import TestCase
import area

class TestShapeAreas(TestCase):
    def test_triangle_area(self):
        self.assertEqual(10, area.triangle_area(4, 5))

    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91))

    def test_triangle_negative_height_base_raises_value_exception(self):

        with self.assertRaises(ValueError):
            area.triangle_area(9, -10)
        
        with self.assertRaises(ValueError):
            area.triangle_area(-9, 10)
        
        with self.assertRaises(ValueError):
            area.triangle_area(-9, -10)

    def test_triangle_area_with_zeroes(self):
        self.assertEqual(0, area.triangle_area(0, 1))
        self.assertEqual(0, area.triangle_area(0, 1))
        self.assertEqual(0, area.triangle_area(0, 0))

    def test_circle_area(self):
        self.assertAlmostEqual(78.5398163, area.circle_area(5))

    def test_circle_area_with_zeroes(self):
        self.assertEqual(0, area.circle_area(0))

    def test_circle_area_with_negative(self):
        with self.assertRaises(ValueError):
            area.circle_area(-5)
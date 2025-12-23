import unittest
import math
import circle
import rectangle
import square
import triangle

class TestCircle(unittest.TestCase):
    def test_area_positive_radius(self):
        """Тест площади круга с положительным радиусом"""
        self.assertAlmostEqual(circle.area(5), math.pi * 25, places=7)

    def test_area_zero_radius(self):
        """Тест площади круга с нулевым радиусом"""
        self.assertAlmostEqual(circle.area(0), 0, places=7)

    def test_area_negative_radius(self):
        """Тест площади круга с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            circle.area(-5)

    def test_perimeter_positive_radius(self):
        """Тест периметра круга с положительным радиусом"""
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5, places=7)

    def test_perimeter_zero_radius(self):
        """Тест периметра круга с нулевым радиусом"""
        self.assertAlmostEqual(circle.perimeter(0), 0, places=7)

    def test_perimeter_negative_radius(self):
        """Тест периметра круга с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            circle.perimeter(-5)

class TestRectangle(unittest.TestCase):
    def test_area_positive_dimensions(self):
        """Тест площади прямоугольника с положительными сторонами"""
        self.assertEqual(rectangle.area(5, 4), 20)

    def test_area_zero_dimensions(self):
        """Тест площади прямоугольника с нулевыми сторонами"""
        self.assertEqual(rectangle.area(0, 4), 0)
        self.assertEqual(rectangle.area(5, 0), 0)
        self.assertEqual(rectangle.area(0, 0), 0)

    def test_area_negative_dimensions(self):
        """Тест площади прямоугольника с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            rectangle.area(-5, 4)
        with self.assertRaises(ValueError):
            rectangle.area(5, -4)
        with self.assertRaises(ValueError):
            rectangle.area(-5, -4)

    def test_perimeter_positive_dimensions(self):
        """Тест периметра прямоугольника с положительными сторонами"""
        self.assertEqual(rectangle.perimeter(5, 4), 18)

    def test_perimeter_zero_dimensions(self):
        """Тест периметра прямоугольника с нулевыми сторонами"""
        self.assertEqual(rectangle.perimeter(0, 4), 8)
        self.assertEqual(rectangle.perimeter(5, 0), 10)

    def test_perimeter_negative_dimensions(self):
        """Тест периметра прямоугольника с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            rectangle.perimeter(-5, 4)
        with self.assertRaises(ValueError):
            rectangle.perimeter(5, -4)

class TestSquare(unittest.TestCase):
    def test_area_positive_side(self):
        """Тест площади квадрата с положительной стороной"""
        self.assertEqual(square.area(5), 25)

    def test_area_zero_side(self):
        """Тест площади квадрата с нулевой стороной"""
        self.assertEqual(square.area(0), 0)

    def test_area_negative_side(self):
        """Тест площади квадрата с отрицательной стороной"""
        with self.assertRaises(ValueError):
            square.area(-5)

    def test_perimeter_positive_side(self):
        """Тест периметра квадрата с положительной стороной"""
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_zero_side(self):
        """Тест периметра квадрата с нулевой стороной"""
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_negative_side(self):
        """Тест периметра квадрата с отрицательной стороной"""
        with self.assertRaises(ValueError):
            square.perimeter(-5)

class TestTriangle(unittest.TestCase):
    def test_area_positive_dimensions(self):
        """Тест площади треугольника с положительными сторонами"""
        self.assertEqual(triangle.area(5, 4), 10)

    def test_area_zero_dimensions(self):
        """Тест площади треугольника с нулевыми размерами"""
        self.assertEqual(triangle.area(0, 4), 0)
        self.assertEqual(triangle.area(5, 0), 0)

    def test_area_negative_dimensions(self):
        """Тест площади треугольника с отрицательными размерами"""
        with self.assertRaises(ValueError):
            triangle.area(-5, 4)
        with self.assertRaises(ValueError):
            triangle.area(5, -4)

    def test_perimeter_positive_sides(self):
        """Тест периметра треугольника с положительными сторонами"""
        self.assertEqual(triangle.perimeter(5, 4, 3), 12)

    def test_perimeter_zero_sides(self):
        """Тест периметра треугольника с нулевыми сторонами"""
        self.assertEqual(triangle.perimeter(0, 4, 3), 7)

    def test_perimeter_negative_sides(self):
        """Тест периметра треугольника с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            triangle.perimeter(-5, 4, 3)
        with self.assertRaises(ValueError):
            triangle.perimeter(5, -4, 3)
        with self.assertRaises(ValueError):
            triangle.perimeter(5, 4, -3)

    def test_triangle_inequality(self):
        """Тест неравенства треугольника"""
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 2, 10) 
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 10, 2) 
        with self.assertRaises(ValueError):
            triangle.perimeter(10, 1, 2) 

    def test_valid_triangle(self):
        """Тест валидного треугольника"""
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)

if __name__ == '__main__':
    unittest.main()
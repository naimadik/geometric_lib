import unittest
import math
import circle
import rectangle
import square
import triangle

class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(5), math.pi * 25, places=7)
    
    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5, places=7)

class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(5, 4), 20)
    
    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(5, 4), 18)

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(5), 25)
    
    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(5, 4), 10)
    
    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(5, 4, 3), 12)

if __name__ == '__main__':
    unittest.main()
import unittest
from main import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_output(self):
        self.assertEqual(fibonacci(2, 2), [4, 6])
        self.assertEqual(fibonacci(1, 9), [2, 3, 5, 8 , 13, 21, 34, 55, 89])
    def test_invalidInput(self):
        with self.assertRaises(TypeError):
            fibonacci("s", 1)
    def test_worksWithoutLength(self):
        self.assertEqual(fibonacci(1), [2, 3, 5, 8 , 13, 21, 34, 55, 89, 144])
        self.assertEqual(fibonacci(5), [10, 15, 25, 40, 65, 105, 170, 275, 445, 720])
        
    
if __name__ == '__main__':
    unittest.main()

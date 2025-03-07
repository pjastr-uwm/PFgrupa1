import unittest
from src.fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):

    def setUp(self):
        pass

    def test_small_integers(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_large_integers(self):
        self.assertEqual(fibonacci(20), 6765)

    def tearDown(self):
        pass
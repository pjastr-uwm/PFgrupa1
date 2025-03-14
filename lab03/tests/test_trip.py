import unittest
from src.trip import Trip


class TestTripInitialization(unittest.TestCase):

    def setUp(self):
        pass

    def test_creation(self):
        trip1 = Trip("Paris", 7)
        self.assertIsInstance(trip1, Trip)

    def test_initilization(self):
        trip1 = Trip("Paris", 7)
        self.assertEqual(trip1.destination, "Paris")
        self.assertEqual(trip1.duration, 7)

    def test_calculate_cost(self):
        trip1 = Trip("Paris", 7)
        self.assertEqual(trip1.calculate_cost(),700)
        trip2 = Trip("Rome", 5)
        self.assertEqual(trip2.calculate_cost(), 500)


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

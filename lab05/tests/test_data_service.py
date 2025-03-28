import unittest
from unittest.mock import Mock
from src.data_service import DataService
from src.task1 import result


class TestDataService(unittest.TestCase):

    def setUp(self):
        self.api_mock = Mock()
        self.service = DataService(self.api_mock)

    def test_fetch_user_data_positive_values(self):
        self.api_mock.get_data.side_effect = ["Jan", "Sylwia"]
        result1 = self.service.fetch_user_data(123)
        self.api_mock.get_data.assert_called_with(123)
        self.assertEqual(result1, "Jan")
        result2 = self.service.fetch_user_data(456)
        self.assertEqual(result2, "Sylwia")



    def tearDown(self):
        pass


if __name__ == "__main __":
    unittest.main()
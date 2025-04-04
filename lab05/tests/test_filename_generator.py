import unittest
from unittest.mock import patch
from datetime import datetime

from src.filename_generator import generate_unique_filename


class TestFilenameGenerator(unittest.TestCase):

    @patch("src.filename_generator.datetime")
    def test_format_positive(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024,2,29,9,12,0)
        result = generate_unique_filename()
        self.assertEqual(result, "file_20240229_091200")

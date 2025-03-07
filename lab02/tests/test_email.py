import unittest
from src.email import validate_email


class TestEmail(unittest.TestCase):

    def setUp(self):
        pass

    def test_email_positive(self):
        # self.assertEqual(validate_email("info@onet.pl"), True)
        self.assertTrue(validate_email("info@onet.pl"))

    def test_email_negative(self):
        self.assertFalse(validate_email("abcyyz"))

    def test_integer_argument(self):
        with self.assertRaises(AttributeError):
            validate_email(3455)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

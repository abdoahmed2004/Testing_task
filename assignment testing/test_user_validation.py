import unittest
from validation import UserValidation

class TestUserValidation(unittest.TestCase):

    
    def test_valid_email(self):
        self.assertTrue(UserValidation.validate_email("abdo@gmail.com"))

    def test_invalid_email(self):
        self.assertFalse(UserValidation.validate_email("abdo@@gmail..com"))

    # Username Tests
    def test_valid_username(self):
        self.assertTrue(UserValidation.validate_username("abdo_123"))

    def test_invalid_username_short(self):
        self.assertFalse(UserValidation.validate_username("ab"))

    # Egyptian Phone Tests
    def test_valid_phone(self):
        self.assertTrue(UserValidation.validate_egyptian_phone("01123456789"))

    def test_invalid_phone_wrong_start(self):
        self.assertFalse(UserValidation.validate_egyptian_phone("01923456789"))

    def test_invalid_phone_short(self):
        self.assertFalse(UserValidation.validate_egyptian_phone("0112345"))

    # Egyptian National ID Tests
    def test_valid_national_id(self):
        self.assertTrue(UserValidation.validate_national_id("29912301234567"))

    def test_invalid_national_id_length(self):
        self.assertFalse(UserValidation.validate_national_id("2991230123456"))

    def test_invalid_national_id_start(self):
        self.assertFalse(UserValidation.validate_national_id("19912301234567"))

if __name__ == '__main__':
    unittest.main()

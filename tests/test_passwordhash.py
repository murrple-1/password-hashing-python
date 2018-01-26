import unittest

import password_hashing


class TestPasswordHash(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hash_of_password = password_hashing.create_hash('password')

    def test_create_hash(self):
        password_hashing.create_hash('test_password')

    def test_successful_validation(self):
        self.assertTrue(
            password_hashing.validate_password(
                'password',
                TestPasswordHash.hash_of_password))

    def test_unsuccessful_validation(self):
        self.assertFalse(
            password_hashing.validate_password(
                'wrong_password',
                TestPasswordHash.hash_of_password))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            password_hashing.validate_password('password', algorithm='')


if __name__ == '__main__':
    unittest.main()

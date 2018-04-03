import unittest

import password_hashing


class TestPasswordHash(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hash_of_b_password = password_hashing.create_hash(b'b_password')
        cls.hash_of_u_password = password_hashing.create_hash(u'u_password')

    def test_create_hash_b(self):
        password_hashing.create_hash(b'test_password')

    def test_create_hash_u(self):
        password_hashing.create_hash(u'test_password')

    def test_successful_validation_b2b(self):
        self.assertTrue(
            password_hashing.validate_password(
                b'b_password',
                TestPasswordHash.hash_of_b_password))

    def test_successful_validation_u2u(self):
        self.assertTrue(
            password_hashing.validate_password(
                u'u_password',
                TestPasswordHash.hash_of_u_password))

    def test_successful_validation_b2u(self):
        self.assertTrue(
            password_hashing.validate_password(
                b'u_password',
                TestPasswordHash.hash_of_u_password))

    def test_successful_validation_u2b(self):
        self.assertTrue(
            password_hashing.validate_password(
                u'b_password',
                TestPasswordHash.hash_of_b_password))

    def test_unsuccessful_validation_b2b(self):
        self.assertFalse(
            password_hashing.validate_password(
                b'wrong_password',
                TestPasswordHash.hash_of_b_password))

    def test_unsuccessful_validation_u2u(self):
        self.assertFalse(
            password_hashing.validate_password(
                u'wrong_password',
                TestPasswordHash.hash_of_u_password))

    def test_unsuccessful_validation_b2u(self):
        self.assertFalse(
            password_hashing.validate_password(
                b'wrong_password',
                TestPasswordHash.hash_of_u_password))

    def test_unsuccessful_validation_u2b(self):
        self.assertFalse(
            password_hashing.validate_password(
                u'wrong_password',
                TestPasswordHash.hash_of_b_password))


if __name__ == '__main__':
    unittest.main()

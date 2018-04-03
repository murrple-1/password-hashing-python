import unittest
import random
import string

import password_hashing


class TestPasswordHash(unittest.TestCase):
    @staticmethod
    def generate_b_str(size=12):
        u_chars = TestPasswordHash.generate_u_str(size=size)
        return u_chars.encode('utf-8')

    @staticmethod
    def generate_u_str(size=12):
        return u''.join(random.choice(string.printable) for _ in range(size))

    @classmethod
    def setUpClass(cls):
        cls.b_password = TestPasswordHash.generate_b_str()
        cls.u_password = TestPasswordHash.generate_u_str()
        cls.u_b_password = cls.b_password.decode('utf-8')
        cls.b_u_password = cls.u_password.encode('utf-8')
        cls.hash_of_b_password = password_hashing.create_hash(cls.b_password)
        cls.hash_of_u_password = password_hashing.create_hash(cls.u_password)

    def test_create_hash_b(self):
        password_hashing.create_hash(TestPasswordHash.generate_b_str())

    def test_create_hash_u(self):
        password_hashing.create_hash(TestPasswordHash.generate_u_str())

    def test_successful_validation_b2b(self):
        self.assertTrue(
            password_hashing.validate_password(
                TestPasswordHash.b_password,
                TestPasswordHash.hash_of_b_password))

    def test_successful_validation_u2u(self):
        self.assertTrue(
            password_hashing.validate_password(
                TestPasswordHash.u_password,
                TestPasswordHash.hash_of_u_password))

    def test_successful_validation_b2u(self):
        self.assertTrue(
            password_hashing.validate_password(
                TestPasswordHash.b_u_password,
                TestPasswordHash.hash_of_u_password))

    def test_successful_validation_u2b(self):
        self.assertTrue(
            password_hashing.validate_password(
                TestPasswordHash.u_b_password,
                TestPasswordHash.hash_of_b_password))

    def test_unsuccessful_validation_b2b(self):
        self.assertFalse(
            password_hashing.validate_password(
                TestPasswordHash.generate_b_str(),
                TestPasswordHash.hash_of_b_password))

    def test_unsuccessful_validation_u2u(self):
        self.assertFalse(
            password_hashing.validate_password(
                TestPasswordHash.generate_u_str(),
                TestPasswordHash.hash_of_u_password))

    def test_unsuccessful_validation_b2u(self):
        self.assertFalse(
            password_hashing.validate_password(
                TestPasswordHash.generate_b_str(),
                TestPasswordHash.hash_of_u_password))

    def test_unsuccessful_validation_u2b(self):
        self.assertFalse(
            password_hashing.validate_password(
                TestPasswordHash.generate_u_str(),
                TestPasswordHash.hash_of_b_password))


if __name__ == '__main__':
    unittest.main()

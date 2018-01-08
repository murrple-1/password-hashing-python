import unittest
from six import print_

import passwordhash

class TestPasswordHash(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hash_of_password = passwordhash.create_hash('password')
        print_('Original Hash: ', cls.hash_of_password)

    def test_create_hash(self):
        passwordhash.create_hash('test_password')

    def test_successful_validation(self):
        self.assertTrue(passwordhash.validate_password('password', TestPasswordHash.hash_of_password))

    def test_unsuccessful_validation(self):
        self.assertFalse(passwordhash.validate_password('wrong_password', TestPasswordHash.hash_of_password))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            passwordhash.validate_password('password', algorithm='')

if __name__ == '__main__':
    unittest.main()


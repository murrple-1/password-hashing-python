# Python implementation of PasswordHash.* (v1.0) https://github.com/defuse/password-hashing
# Requires Python >= v2.7.9, due to https://www.python.org/dev/peps/pep-0466/#new-security-related-features-in-python-2-7-maintenance-releases
# Please note, this code has not been scrutinized or peer-reviewed at all. It is a naive attempt to re-implement PasswordHash.php.

import os
import base64
import hashlib

# These constants may be changed without breaking existing hashes.
PBKDF2_ALGORITHM = 'sha256'
PBKDF2_ITERATIONS = 1000
PBKDF2_SALT_BYTE_SIZE = 24
PBKDF2_HASH_BYTE_SIZE = 24

# format: algorithm:iterations:salt:hash
def createHash(password, algorithm=PBKDF2_ALGORITHM, iterations=PBKDF2_ITERATIONS, saltByteSize=PBKDF2_SALT_BYTE_SIZE, hashByteSize=PBKDF2_HASH_BYTE_SIZE):
    salt = base64.b64encode(os.urandom(saltByteSize))
    hash = hashlib.pbkdf2_hmac(algorithm, password, salt, iterations)[0:hashByteSize]
    return '{0}:{1}:{2}:{3}'.format(algorithm, iterations, salt, base64.b64encode(hash))

def validatePassword(password, correctHash):
    params = correctHash.split(':')
    if len(params) != 4:
        return False

    algorithm = params[0]
    iterations = int(params[1])
    salt = params[2]
    hash = base64.b64decode(params[3])

    computedHash = hashlib.pbkdf2_hmac(algorithm, password, salt, iterations)[0:len(hash)]

    return _slowEquals(hash, computedHash)

# via https://github.com/PeterScott/streql
def _slowEquals(x, y):
  """Does x == y? Runtime does not depend on the bytes in the strings."""
  if len(x) != len(y):
    return False

  result = 0
  for i in xrange(len(x)):
    result |= ord(x[i]) ^ ord(y[i])
  return result == 0

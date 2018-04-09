# password-hashing-python

[![Build Status](https://travis-ci.org/murrple-1/password-hashing-python.svg?branch=master)](https://travis-ci.org/murrple-1/password-hashing-python) [![Coverage Status](https://coveralls.io/repos/github/murrple-1/password-hashing-python/badge.svg?branch=master)](https://coveralls.io/github/murrple-1/password-hashing-python?branch=master)

Python implementation of https://github.com/defuse/password-hashing (v1.0)

Supports both Python `>=v2.7.9` and `>=3.4`.

Please note, this code has not been scrutinized or peer-reviewed at all - though I'm interested, if anyone wants to look it over.

It is a naive attempt to re-implement `PasswordHash.php`.

# Installation

`pip install password-hashing-python`

# Usage

## Creating a hash-string
```Python Console
>>> import password_hashing
>>> _hash = password_hashing.create_hash('your_password')
>>> print _hash
b'sha1:64000:18:B6oWbvtHvu8qCgoE75wxmvpidRnGzGFt:R1gkPOuVjqIoTulWP1TABS0H'
>>> # snip: save `_hash` to a DB
```

## Validating the password
```Python Console
>>> # snip: retrieve `_hash` from DB
>>> import password_hashing
>>> password_hashing.validate_password('your_password', _hash)
True
>>> password_hashing.validate_password('wrong_password', _hash)
False
```

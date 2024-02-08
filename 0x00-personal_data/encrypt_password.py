#!/usr/bin/env python3
"""implementing Passwords"""

import bcrypt


def hash_password(password):
    """encrypting Password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password, password):
    """check validity of passsword"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
#!/usr/bin/python3

import bcrypt

"""Auth Stuff"""

def _hash_password(password: str) -> bytes:
    """Hash Password"""

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

"""
AlmaLinux Build System hashing functions.
"""

import hashlib


def get_hasher(checksum_type):
    """
    Returns a corresponding hashlib hashing function for the specified checksum
    type.

    Parameters
    ----------
    checksum_type : str
        Checksum type (e.g. sha1, sha256).

    Returns
    -------
    _hashlib.HASH
        Hashlib hashing function.
    """
    return hashlib.new("sha256" if checksum_type == "sha" else checksum_type)


def hash_password(password, salt):
    """
    Returns a SHA256 password hash.

    Parameters
    ----------
    password : str
        Password to hash.
    salt : str
        Password "salt".

    Returns
    -------
    str
        SHA256 password hash.
    """
    return str(hashlib.sha256((salt + password).encode("utf-8")).hexdigest())

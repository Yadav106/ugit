import os
import hashlib

GIT_DIR = ".ugit"

def init():
    """
    Initialize a custom Git-like repository.

    Args:
        None

    Returns:
        str: Message indicating success or if the repository already exists.
    """
    try:
        os.makedirs(GIT_DIR)
        os.makedirs(os.path.join(GIT_DIR, 'objects'))
        return f"Initialized empty ugit repository in {os.path.join(os.getcwd(), GIT_DIR)}"
    except FileExistsError:
        return f"A ugit repository already exists in {os.getcwd()}"

def hash_object(data):
    """
    Hashes a given file and stores it in .ugit/objects/

    Args:
        data - str: the contents of the file to be hashed

    Returns:
        oid - str: the object id of the hashed file
    """
    oid = hashlib.sha1(data).hexdigest()
    with open(f"{GIT_DIR}/objects/{oid}", "wb") as out:
        out.write(data)
    return oid

def get_object(oid):
    """
    Returns the contents of a hashed object

    Args:
        oid - str: the object id of the hashed file

    Returns:
        str: the contents of the hashed file
    """
    with open(f"{GIT_DIR}/objects/{oid}", "rb") as f:
        return f.read()

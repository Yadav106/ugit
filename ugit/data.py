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

def hash_object(data, type_="blob"):
    """
    Hashes a given file and stores it in .ugit/objects/

    Args:
        data - str: the contents of the file to be hashed

    Returns:
        oid - str: the object id of the hashed file
    """
    obj = type_.encode() + b'\x00' + data
    oid = hashlib.sha1(data).hexdigest()
    with open(f"{GIT_DIR}/objects/{oid}", "wb") as out:
        out.write(obj)
    return oid

def get_object(oid, expected:str|None="blob"):
    """
    Returns the contents of a hashed object

    Args:
        oid - str: the object id of the hashed file

    Returns:
        str: the contents of the hashed file
    """
    with open(f"{GIT_DIR}/objects/{oid}", "rb") as f:
        obj = f.read()

    type_, _, content = obj.partition(b'\x00')
    type_ = type_.decode()

    if expected is not None:
        assert type_ == expected, f'Expected {expected}, got {type_}'

    return content

def set_HEAD(oid):
    with open(f"{GIT_DIR}/HEAD", "w") as f:
        f.write(oid)

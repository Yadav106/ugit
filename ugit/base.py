import os
from ugit import data

def write_tree(directory=".") -> str:
    entries = []

    with os.scandir(directory) as it:
        for entry in it:
            full = os.path.join(directory, entry.name)
            if is_ignored(full):
                continue

            if entry.is_file(follow_symlinks=False):
                type_ = "blob"
                with open(full, 'rb') as f:
                    oid = data.hash_object(f.read())
            elif entry.is_dir(follow_symlinks=False):
                type_ = "tree"
                oid = write_tree(full)
            else: # initialize type_ and oid with empty valyes
                type_ = ""
                oid = ""

            entries.append((entry.name, oid, type_))

    tree = "".join(f"{type_} {oid} {name}\n"
                   for name, oid, type_
                   in sorted(entries))

    return data.hash_object(tree.encode(), "tree")


def is_ignored(path:str):
    return '.ugit' in path.split('/')

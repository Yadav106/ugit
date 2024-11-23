import os
from ugit import data

def write_tree(directory="."):
    with os.scandir(directory) as it:
        for entry in it:
            full = os.path.join(directory, entry.name)
            if is_ignored(full):
                continue

            if entry.is_file(follow_symlinks=False):
                print(full)
            elif entry.is_dir(follow_symlinks=False):
                write_tree(full)


def is_ignored(path:str):
    return '.ugit' in path.split('/')

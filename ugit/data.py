import os

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
        return f"Initialized empty ugit repository in {os.path.join(os.getcwd(), GIT_DIR)}"
    except FileExistsError:
        return f"A ugit repository already exists in {os.getcwd()}"

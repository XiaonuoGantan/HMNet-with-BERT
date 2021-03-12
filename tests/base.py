import os


def data_dirpath() -> str:
    """Return the path to the directory that stores the preprocessed .jsonl.gz meeting data"""
    return os.path.join(os.path.dirname(__file__), "../data")

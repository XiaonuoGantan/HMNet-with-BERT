import gzip
import json
from typing import Dict


def read_jsonl_gz_data(filepath: str) -> Dict:
    """Gunzip and then read a .jsonl data file"""
    with gzip.open(filepath, "r") as fp:
        return json.load(fp)

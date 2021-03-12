import os
import pytest

from datasets.base import read_jsonl_gz_data
from tests.base import data_dirpath


@pytest.mark.unittest
def test_read_jsonl_gz_data():
    """split_1.jsonl looks like:

    {
        "id": "IS1007a",
        "meeting": [...],
        "summary": [...]
    }
    """
    filepath = os.path.join(data_dirpath(), "AMI_proprec/dev/split_1.jsonl.gz")
    data = read_jsonl_gz_data(filepath)
    assert data["id"] == "IS1007a"
    assert isinstance(data["meeting"], list)
    assert isinstance(data["summary"], list)

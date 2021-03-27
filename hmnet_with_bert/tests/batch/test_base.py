import json
from typing import Dict

import pytest
import toml

from hmnet_with_bert.batch.base import HMNetWithBertBatchGen


def dev_conf() -> Dict:
    with open("conf/dev_pretrain.toml", "r") as fp:
        return toml.load(fp)


@pytest.mark.unittest
def test_HMNetWithBertBatchGen__verify():
    gen = HMNetWithBertBatchGen(dev_conf())
    assert gen.role_dict_filepath == "data/role_dict_ext.json"

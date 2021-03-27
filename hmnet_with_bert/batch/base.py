import json
import os

from typing import Dict, Optional


class HMNetWithBertBatchGen(object):
    """Data pre-processing and loader by batches"""

    def __init__(self, conf: Dict):
        self._verify(conf)
        self.conf = conf

    @property
    def role_dict(self) -> Optional[Dict]:
        """Return the meeting-role dictionary"""
        if self.role_dict_filepath:
            with open(self.role_dict_filepath, "r") as fp:
                return json.load(fp)
        return None

    @property
    def role_dict_filepath(self) -> Optional[str]:
        """Return the role dictionary's conf filepath, if configured"""
        filepath = os.path.join(self.conf["data"]["dir"], self.conf["data"]["role_dict"])
        if os.path.exists(filepath):
            return filepath
        return None

    def _verify(self, conf: Dict):
        """Verify if `conf` is valid or not not and raise a ValueError if it is not"""
        if "data" not in conf:
            raise ValueError(f"HMNetWithBertBatchGen._verify: 'data' is not specified in {conf}")
        if "role_dict" not in conf["data"]:
            raise ValueError(f"HMNetWithBertBatchGen._verify: 'role_dict' is not specified in 'data' of {conf}")

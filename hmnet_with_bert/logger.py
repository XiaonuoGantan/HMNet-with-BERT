import logging
from typing import Dict


def logger(conf: Dict) -> logging.Logger:
    """Return a logger instance configured according to `conf` from """
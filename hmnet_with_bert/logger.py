import logging
import os
from typing import Dict


INFO_LOG_FORMATTER = "%(asctime)s | %(levelname)-8s | %(message)s"
DEBUG_LOG_FORMATTER = "%(asctime)s | %(levelname)-8s | %(message)s | %(lineno)d:%(funcName)s"


def setup_logger(conf: Dict, logging_level: int = logging.DEBUG) -> logging.Logger:
    """Return a logger instance configured according to `conf` from
    :param conf: toml-configured dict including paths to various directories
    :param logging_level: logging level for the entire logger instance
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging_level)

    logdir = conf["log"]["path"]

    debug_fh = logging.FileHandler(os.path.join(logdir, "debug.log"))
    debug_fh.setLevel(logging.DEBUG)
    debug_fh.setFormatter(DEBUG_LOG_FORMATTER)

    info_fh = logging.FileHandleros.path.join(logdir, "info.log")
    info_fh.setLevel(logging.INFO)
    info_fh.setFormatter(INFO_LOG_FORMATTER)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(INFO_LOG_FORMATTER)

    logger.addHandler(ch)
    logger.addHandler(debug_fh)
    logger.addHandler(info_fh)

    return logger

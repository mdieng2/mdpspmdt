#!/usr/bin/env python
# -*- coding:Utf-8 -*-

"""

"""
__author__ = "Moussa DIENG"
__copyright__ = "Copyright 2018, Ingenico FR"
__credits__ = ["Moussa DIENG (Ingenico Partner)"]
__license__ = "Ingenico Internal Licence"
__version__ = "1.0.2"
__maintainer__ = "Moussa DIENG"
__email__ = "moussa.dieng@ingenico.com"
__status__ = "Development"

import os
import logging
from logging.handlers import TimedRotatingFileHandler


logger_directory = "C:\Program Files\Ingenico\Depackager\log"


def _manage_directory(file_path):
    directory = os.path.dirname(file_path)

    try:
        os.stat(directory)
    except:
        os.makedirs(directory)

def init_logger(logger_name="depackager", log_file=logger_directory + "\log_depackager.log"):
    _manage_directory(log_file)
    logger = logging.getLogger(logger_name)
    # hdlr = logging.FileHandler(log_file)
    handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1)
    handler.suffix = "%Y%m%d"
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def log_error(logger, error_msg):
    logger.setLevel(logging.ERROR)
    logger.error(error_msg)


def log_info(logger, info_msg):
    logger.setLevel(logging.INFO)
    logger.info(info_msg)


def log_debug(logger, debug_msg):
    logger.setLevel(logging.DEBUG)
    logger.debug(debug_msg)


def log_warning(logger, warning_msg):
    logger.setLevel(logging.WARNING)
    logger.warning(warning_msg)


def log_warn(logger, warn_msg):
    logger.setLevel(logging.WARNING)
    logger.warn(warn_msg)


def log_critical(logger, critical_msg):
    logger.setLevel(logging.CRITICAL)
    logger.critical(critical_msg)
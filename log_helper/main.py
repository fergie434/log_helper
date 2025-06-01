#!/usr/bin/env python3
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(log_directory='logs', log_filename='log.log', log_maxbytes=4000000, log_filecount=5):
    log_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), log_directory, log_filename)
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
    )
    rotating_handler = RotatingFileHandler(filename=log_filename, maxBytes=log_maxbytes, backupCount=log_filecount)
    rotating_handler.setFormatter(formatter)
    logger.addHandler(rotating_handler)

    return logger

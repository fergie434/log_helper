#!/usr/bin/env python3
import logging
from logging.handlers import RotatingFileHandler
import os
import sys
from pathlib import Path

def setup_logging(log_filename='log.log', log_maxbytes=4000000, log_filecount=5, log_directory='logs', log_level=logging.INFO):
    log_filepath = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), log_directory)
    log_filename = os.path.join(log_filepath, log_filename)

    Path(log_filepath).mkdir(exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.setLevel(level=log_level)
    formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
    )
    rotating_handler = RotatingFileHandler(filename=log_filename, maxBytes=log_maxbytes, backupCount=log_filecount)
    rotating_handler.setFormatter(formatter)
    logger.addHandler(rotating_handler)

    return logger

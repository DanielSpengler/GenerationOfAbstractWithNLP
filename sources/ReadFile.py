"""
Read contents of textfiles into memory
"""

import logging
import os

logger = logging.getLogger(__name__)


def load_text(input_file):
    logger.info("Checking if file %s exists...", input_file)
    if os.path.exists(input_file):
        logger.info("File found. Trying to open...")
        with open(input_file, mode="r", encoding="utf8") as infile:
            logger.info("Open successfull")
            return infile.read()

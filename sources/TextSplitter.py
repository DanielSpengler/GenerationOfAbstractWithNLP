"""
Split text on a chapter basis
"""

import logging
import re

REGEX_ROMAN_NUMERALS = '[MDCLXVI]+'
REGEX_CHAPTER_POINT = '\.'

logger = logging.getLogger(__name__)

def split_text_into_chapters(text):
    logger.info("Splitting text into chapters")
    regexp = REGEX_ROMAN_NUMERALS + REGEX_CHAPTER_POINT
    #result = re.split(regexp, text)
    result = re.split(r' [XVI]+\. ', text, flags=re.IGNORECASE)

    #logger.info("Removing value before first chapter")
    #result = result[1:]

    logger.info(f"Found {len(result)} chapters in text")
    return result
"""
Pre-Process text for usage in Transformer
"""

import logging

logger = logging.getLogger(__name__)

REFERENCES = 'REFERENCES'
INTRODUCTION = 'INTRODUCTION'

def preprocess_text(raw_data: str):
    logger.info("Starting text preprocessing...")
    clean_text = raw_data

    logger.info("Checking for introduction...")
    if INTRODUCTION in clean_text:
        logger.info("Removing text before introduction")
        clean_text = ''.join(clean_text.partition(INTRODUCTION)[1:])

    logger.info(f"Checking for references chapter...")
    if REFERENCES in clean_text:
        logger.info("Removing references...")
        clean_text = clean_text.partition(REFERENCES)[0]

    logger.info("Removing leading and trailing whitespaces...")
    clean_text = clean_text.strip()

    
    logger.info("Done preprocessing")
    return clean_text
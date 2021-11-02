"""
Pre-Process text for usage in Transformer
"""

import logging

logger = logging.getLogger(__name__)

REFERENCES = 'REFERENCES'
INTRODUCTION = 'INTRODUCTION'


def remove_text_before_introduction(raw_data: str):
    logger.info("Checking for introduction...")
    clean_text = raw_data
    if INTRODUCTION in clean_text:
        logger.info("Removing text before introduction")
        clean_text = ''.join(clean_text.partition(INTRODUCTION)[1:])
    return clean_text

def remove_text_after_references(raw_data: str):
    logger.info(f"Checking for references chapter...")
    clean_text = raw_data
    if REFERENCES in clean_text:
        logger.info("Removing references...")
        clean_text = clean_text.partition(REFERENCES)[0]
    return clean_text

def remove_leading_trailing_whitespaces(raw_data: str):
    logger.info("Removing leading and trailing whitespaces...")
    clean_text = raw_data
    clean_text = clean_text.strip()
    return clean_text

def remove_linebreaks(raw_data: str):
    logger.info("Removing leading and trailing whitespaces...")
    clean_text = raw_data.replace("\n"," ")
    return clean_text


def preprocess_text(raw_data: str):
    logger.info("Starting text preprocessing...")
    clean_text = raw_data

    #remove text before introduction
    clean_text = remove_text_before_introduction(clean_text)

    #remove text after references
    clean_text = remove_text_after_references(clean_text)

    #remove whitespaces
    clean_text = remove_leading_trailing_whitespaces(clean_text)
    
    #remove newlines
    clean_text = remove_linebreaks(clean_text)

    logger.info("Done preprocessing")
    return clean_text
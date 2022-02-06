"""
Pre-Process text for usage in Transformer
"""

import logging
import re

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

def remove_authorization_note(raw_data: str):
    logger.info("Removing authorization note...")
    clean_text = raw_data
    clean_text = re.sub(r'Authorized licensed .* Restrictions apply\.', ' ', raw_data)
    return clean_text

def remove_non_unicode_characters(raw_data: str):
    logger.info("Removing non-whitespaces characters...")
    clean_text = raw_data
    clean_text = re.sub(r'\(cid:\d*\)', ' ', raw_data)
    return clean_text

def remove_leading_trailing_whitespaces(raw_data: str):
    logger.info("Removing leading and trailing whitespaces...")
    clean_text = raw_data
    clean_text = clean_text.strip()
    return clean_text

def remove_linebreaks(raw_data: str):
    logger.info("Removing linebreaks...")
    clean_text = raw_data.replace("\n"," ")
    return clean_text

def remove_double_spaces(raw_data: str):
    logger.info("Removing double spaces within the text...")
    clean_text = re.sub('\s{2,}', ' ', raw_data)
    return clean_text
    

def preprocess_text(raw_data: str, remove_beginning=True, remove_end=True):
    logger.info("Starting text preprocessing...")
    clean_text = raw_data

    if remove_beginning:
        #remove text before introduction
        clean_text = remove_text_before_introduction(clean_text)
    if remove_end:
        #remove text after references
        clean_text = remove_text_after_references(clean_text)

    #remove special characters (cid:xx)
    clean_text = remove_non_unicode_characters(clean_text)

    #remove leading/trailing whitespaces
    clean_text = remove_leading_trailing_whitespaces(clean_text)
    
    #remove newlines
    clean_text = remove_linebreaks(clean_text)

    #remove double spaces
    clean_text = remove_double_spaces(clean_text)

    logger.info("Done preprocessing")
    return clean_text
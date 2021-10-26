"""
Read contents of textfiles into memory
"""

import logging
import os
from pdfminer.high_level import extract_text

logger = logging.getLogger(__name__)
logging.getLogger("pdfminer").setLevel(logging.ERROR)

#TODO maybe add support for latex documents

def read_from_pdf(input_file):
    """
    Loads text from pdf files
    """
    logger.info("Starting textract to read PDF...")
    logger.info(f"inputfile: {input_file}")
    text = extract_text(input_file)
    logger.info("Done reading file")
    return text

def read_from_txt(input_file):
    """
    Loads text from simple txt files
    """
    with open(input_file, mode="r", encoding="utf8") as infile:
        logger.info("Open successfull")
        return infile.read()

switcher = {
    ".pdf": read_from_pdf,
    ".txt": read_from_txt,
    }

def load_file(input_file):
    logger.info("Checking if file %s exists...", input_file)
    if os.path.exists(input_file):
        logger.info("File found. Analyzing file type...")
        
        extension = os.path.splitext(input_file)[1]
        logger.info("Found extension: %s", extension)

        func = switcher.get(extension, lambda x: "Invalid option")
        logger.info("Found consumer: %s", func)
        return func(input_file)

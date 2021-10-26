"""
Pre-Process text for usage in Transformer
"""

import logging

logger = logging.getLogger(__name__)


def preprocess_text(raw_data):
    logger.info("Starting text preprocessing...")
    clean_text = raw_data.strip()
    return clean_text
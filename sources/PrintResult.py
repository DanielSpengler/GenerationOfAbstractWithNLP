"""
Print results into files
"""

import logging
import os
import errno

logger = logging.getLogger(__name__)

DEFAULT_EXTENSION = "txt"


def dump_text_to_file(data, path, name, extension=DEFAULT_EXTENSION):
    """
    Dumps given data into file with the structure: results/name
    """
    logger.info("Starting dump to new directory")
    #check if directory exists
    filename = f"{name}.{extension}"
    logger.info("Filepath: %s", filename)
    i = 0
    while os.path.exists(os.path.join(path, filename)):
        logger.info("File already exists.")
        logger.info("Adding number to it")
        i += 1
        filename = f"{name}{i}.{extension}"

    filename = os.path.join(path, filename)

    #dump data to file
    with open(filename, "w", encoding="utf-8") as outfile:
        logger.info("Creating file: %s", outfile.name)
        outfile.write(data)
        logger.info("Dumped data into output file %s", outfile.name)
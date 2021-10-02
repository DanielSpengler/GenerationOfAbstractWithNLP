"""
Handle the general workflow of the Abstract generation
"""

from logging.config import fileConfig
import logging
import PrintResult

logging.config.fileConfig('config/logging_config.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

RESULT_PATH = "results"
FILE_EXTENSION = "txt"

def main():
    #load text into memory

    #setup transformer

    #run model

    #generate abstract

    #print abstract to file
    filename = "generated"
    data = "Hello World"
    PrintResult.dump_text_to_file(RESULT_PATH, filename, FILE_EXTENSION, data)

    return


if __name__ == '__main__':
    main()
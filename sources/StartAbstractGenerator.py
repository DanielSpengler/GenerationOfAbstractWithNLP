"""
Handle the general workflow of the Abstract generation
"""

from logging.config import fileConfig
import logging
import PrintResult
import ReadFile

logging.config.fileConfig('config/logging_config.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

INPUT_PATH = "inputs"
RESULT_PATH = "results"

def main():
    #load text into memory
    input_filename = "loremipsum.txt"
    raw_data = ReadFile.load_text(f"{INPUT_PATH}/{input_filename}")

    #setup transformer

    #run model

    #generate abstract
    data = raw_data

    #print abstract to file
    filename = "generated"
    PrintResult.dump_text_to_file(data, RESULT_PATH, filename)

    return


if __name__ == '__main__':
    main()
"""
Handle the general workflow of the Abstract generation
"""

from logging.config import fileConfig
import logging
import os

import PrintResult
import ReadFile

logging.config.fileConfig('config/logging_config.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

INPUT_PATH = "inputs"
RESULT_PATH = "results"

def start_process(input_filename=None, output_filename=None):
    #load text into memory
    if input_filename == None:
        input_filename="loremipsum.txt"
    raw_data = ReadFile.load_text(os.path.join(INPUT_PATH, input_filename))

    #TODO set up transformer
    #setup transformer

    #run model

    #generate abstract
    data = raw_data

    #print abstract to file
    if output_filename == None:
    #TODO generate a clever name OR take from call argument
        output_filename = "generated"

    PrintResult.dump_text_to_file(data, RESULT_PATH, output_filename)

    return


if __name__ == '__main__':
    start_process()
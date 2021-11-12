"""
Handle the general workflow of the Abstract generation
"""

from logging.config import fileConfig
import logging
import os

from . import PrintResult
from . import ReadFile
from . import TextPreprocessor
from . import TextSplitter
from . import TransformerUtils

logging.config.fileConfig('config/logging_config.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

INPUT_PATH = "inputs"
RESULT_PATH = "results"

def start_process(input_filename=None, output_filename=None):
    #load text into memory
    if input_filename == None:
        input_filename="loremipsum.txt"

    raw_data = ReadFile.load_file(os.path.join(INPUT_PATH, input_filename))

    #preprocess text to make it accessible for Transformer
    data = TextPreprocessor.preprocess_text(raw_data)

    #split text into chapters
    chapters = TextSplitter.split_text_into_chapters(data)

    #generate summary for each chapter
    chapter_summaries = []
    for chapter in chapters:
        prepocessed_chapter = TextPreprocessor.preprocess_text(chapter, False, False)
        #T5 variant
        #chapter_summary = TransformerUtils.start_Transformer('t5', prepocessed_chapter)
        #Longformer variant
        #chapter_summary = TransformerUtils.start_Transformer('longformer', prepocessed_chapter)
        chapter_summary = prepocessed_chapter
        chapter_summaries.append(chapter_summary)
    
    #build summary from chapter summaries
    summary = "\n".join(chapter_summaries)

    #print abstract to file
    if output_filename == None:
    #TODO generate a clever name OR take from call argument
        output_filename = "generated"

    PrintResult.dump_text_to_file(summary, RESULT_PATH, output_filename)

    return


if __name__ == '__main__':
    start_process()
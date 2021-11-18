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


def summarize_on_chapter_basis(transformer_type, preprocessed_text):
    """
    summarize text on basis of chapters
    """

    #split text into chapters
    chapters = TextSplitter.split_text_into_chapters(preprocessed_text)

    #generate summary for each chapter
    chapter_summaries = []
    for idx, chapter in enumerate(chapters):
        logger.info(f"Summarizing chapter {idx}/{len(chapters)}")
        chapter_summary = ""
        prepocessed_chapter = TextPreprocessor.preprocess_text(chapter, False, False)
    
        chapter_summary = TransformerUtils.start_Transformer(transformer_type, prepocessed_chapter)

        chapter_summaries.append(chapter_summary)

    TransformerUtils.stop_transformer(transformer_type)

    #build summary from chapter summaries
    summary = "\n".join(chapter_summaries)

    return summary

def summarize_complete_text(transformer_type, preprocessed_text):
    summary = TransformerUtils.start_Transformer(transformer_type, preprocessed_text)

    TransformerUtils.stop_transformer(transformer_type)

    return summary

def start_process(input_filename=None, output_filename=None, transformer_type=None, based_on_chapters:bool=False):
    #load text into memory
    if input_filename == None:
        input_filename="loremipsum.txt"
    
    if transformer_type == None:
        #T5 variant
        transformer_type = 't5'
        #Longformer variant
        #transformer_type = 'longformer'

    raw_data = ReadFile.load_file(os.path.join(INPUT_PATH, input_filename))

    #preprocess text to make it accessible for Transformer
    data = TextPreprocessor.preprocess_text(raw_data)
    
    if based_on_chapters:
        logger.info("Summarizing on chapter basis")
        summary = summarize_on_chapter_basis(transformer_type, data)
    else:
        logger.info("Summarizing complete text")
        summary = summarize_complete_text(transformer_type, data)

    #print abstract to file
    if output_filename == None:
        output_filename = "summary"

    chapterized = "chapterized" if based_on_chapters else "complete"
    output_filename = f"{transformer_type}_{chapterized}_summary_{output_filename}"

    PrintResult.dump_text_to_file(summary, RESULT_PATH, output_filename)

    return


if __name__ == '__main__':
    start_process()
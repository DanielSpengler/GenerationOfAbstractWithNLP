#!/usr/bin/python
# -*- coding: utf-8 -*-
import optparse
import os, sys
import logging


from sources import AbstractGenerator
from sources import ReadFile

def main():
    logger = logging.getLogger(__name__)
    
    logger.info("Now Chen")
    input_file = "chen_2019.pdf"

    outputfile = "chen_2019"

    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='t5', based_on_chapters=True, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='t5', based_on_chapters=False, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='longformer', based_on_chapters=True, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='longformer', based_on_chapters=False, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='roberta', based_on_chapters=True, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='roberta', based_on_chapters=False, into_Folder=True)

    logger.info("\n\nNow Tang")
    
    input_file = "tang_2020.pdf"

    outputfile = "tang_2020"

    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='t5', based_on_chapters=True, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='t5', based_on_chapters=False, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='longformer', based_on_chapters=True, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='longformer', based_on_chapters=False, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='roberta', based_on_chapters=True, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='roberta', based_on_chapters=False, into_Folder=True)
    
    
    logger.info("\n\nNow Ko")
    input_file = "ko_2014.pdf"

    outputfile = "ko_2014"

    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='t5', based_on_chapters=True, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='t5', based_on_chapters=False, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='longformer', based_on_chapters=True, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='longformer', based_on_chapters=False, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='roberta', based_on_chapters=True, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='roberta', based_on_chapters=False, into_Folder=True)


if __name__ == '__main__':
    main()

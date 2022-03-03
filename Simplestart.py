#!/usr/bin/python
# -*- coding: utf-8 -*-
import optparse
import os, sys
import logging


from sources import AbstractGenerator

def main():
    logger = logging.getLogger(__name__)
    
    logger.info("\n\nNow Chen")
    input_file = "chen_2019.pdf"

    outputfile = "chen_2019"
    #AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='longformer', based_on_chapters=False)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='roberta', based_on_chapters=True)
    
    logger.info("#################")
    logger.info("\n\nNow Tang")
    
    input_file = "tang_2020.pdf"

    outputfile = "tang"

    #AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='longformer', based_on_chapters=False)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='roberta', based_on_chapters=True)
    
    logger.info("#################")
    logger.info("\n\nNow Ko")
    input_file = "ko_2014.pdf"

    outputfile = "ko_2014"

    #AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='longformer', based_on_chapters=False)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='roberta', based_on_chapters=True)

if __name__ == '__main__':
    main()

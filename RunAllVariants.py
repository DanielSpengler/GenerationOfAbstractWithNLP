#!/usr/bin/python
# -*- coding: utf-8 -*-
import optparse
import os, sys


from sources import AbstractGenerator
from sources import ReadFile

def main():
    
    input_file = "devops_article.pdf"

    outputfile = "devops"

    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='t5', based_on_chapters=False, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='t5', based_on_chapters=True, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='longformer', based_on_chapters=False, into_Folder=True)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='longformer', based_on_chapters=True, into_Folder=True)

if __name__ == '__main__':
    main()

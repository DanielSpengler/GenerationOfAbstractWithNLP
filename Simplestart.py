#!/usr/bin/python
# -*- coding: utf-8 -*-
import optparse
import os, sys


from sources import AbstractGenerator

def main():
    
    input_file = "devops_article.pdf"

    outputfile = "devops"

    #AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type='longformer', based_on_chapters=False)
    AbstractGenerator.start_process(input_filename=input_file, output_filename=outputfile, transformer_type=None, based_on_chapters=False)

if __name__ == '__main__':
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
import optparse
import os, sys


from sources import StartAbstractGenerator
from sources import ReadFile

def main():
    
    input_file = "devops_article.pdf"

    outputfile = "summary"

    StartAbstractGenerator.start_process(input_file, outputfile)

if __name__ == '__main__':
    main()

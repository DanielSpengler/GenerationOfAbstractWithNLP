#!/usr/bin/python
# -*- coding: utf-8 -*-
import optparse
import os, sys


from sources import AbstractGenerator


def main():
    parser = optparse.OptionParser("usage %prog "+\
      "-f <zipfile> -d <dictionary>")
    parser.add_option('-i', dest='inputfile', type='string',\
      help='specify inputfile')
    parser.add_option('-o', dest='outputfile', type='string',\
      help='specify output name')
    (options, args) = parser.parse_args()
    if (options.inputfile == None) | (options.outputfile == None):
        print(parser.usage)
        exit(0)
    else:
        inputfile = options.inputfile
        outputfile = options.outputfile

    AbstractGenerator.start_process(inputfile, outputfile)

if __name__ == '__main__':
    main()


from sources import ReadFile

import os
import logging

TESTFILE_PATH = "tests/inputs"
TESTFILE_NAME = "loremipsum"
SWITCHER_TESTFILE = "switcher_file"
FILE_CONTENTS = "Lorem ipsum dolor sit amet"

def read_file(fileextension):
    file = f"{TESTFILE_NAME}.{fileextension}"
    return ReadFile.load_file(os.path.join(TESTFILE_PATH, file))


def test_reading_txt_file():
    """
    test reading of simple file
    """
    fileextension = "txt"
    file = f"{TESTFILE_NAME}.{fileextension}"
    result = ReadFile.read_from_txt(os.path.join(TESTFILE_PATH, file))
    assert result == FILE_CONTENTS

def test_reading_pdf_file():
    """
    test reading of pdf file
    """
    fileextension = "pdf"
    file = f"{TESTFILE_NAME}.{fileextension}"
    result = ReadFile.read_from_pdf(os.path.join(TESTFILE_PATH, file))
    assert result.strip() == FILE_CONTENTS


def test_switcher_with_corresponding_file():
    """
    test the switcher funcionality in load_file
    """
    #test txt
    fileextension = "txt"
    file = f"{SWITCHER_TESTFILE}.{fileextension}"
    result = ReadFile.load_file(os.path.join(TESTFILE_PATH, file))
    assert result == f"text in {fileextension}-format"

    #test pdf
    fileextension = "pdf"
    file = f"{SWITCHER_TESTFILE}.{fileextension}"
    result = ReadFile.load_file(os.path.join(TESTFILE_PATH, file))
    assert result.strip() == f"text in {fileextension}-format"
    
    #test unrecognized
    fileextension = "dat"
    file = f"{SWITCHER_TESTFILE}.{fileextension}"
    result = ReadFile.load_file(os.path.join(TESTFILE_PATH, file))
    assert result == "Invalid option"


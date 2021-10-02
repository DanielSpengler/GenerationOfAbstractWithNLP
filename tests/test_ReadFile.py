
from sources import ReadFile

import os
import logging

TESTFILE_PATH = "tests/inputs"
TESTFILE_NAME = "loremipsum.txt"
FILE_CONTENTS = "Lorem ipsum dolor sit amet"

def read_file():
    return ReadFile.load_text(os.path.join(TESTFILE_PATH, TESTFILE_NAME))


def test_reading_simplte_file(caplog):
    """
    test reading of simple file
    """
    assert read_file() == FILE_CONTENTS



from sources import PrintResult
import os
import errno

TESTFILE_PATH = "tests/test_results"
TESTFILE_NAME = "testfile"
TEST_DATA = "This file was created by a unit test."

def create_results_folder(filepath):
    if not os.path.exists(filepath):
        try:
            os.makedirs(filepath)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

def create_test_file():
    #create_results_folder(TESTFILE_PATH)
    PrintResult.dump_text_to_file(TEST_DATA, TESTFILE_PATH, TESTFILE_NAME)

def setup_module():
    if not os.path.exists(TESTFILE_PATH):
        try:
            os.makedirs(TESTFILE_PATH)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

def teardown_module():
    if os.path.exists(TESTFILE_PATH):
        try:
            for file in os.scandir(TESTFILE_PATH):
                os.unlink(file.path)
            os.removedirs(TESTFILE_PATH)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

def test_creation_of_first_file():
    """
    test creation of first file
    """
    create_test_file()
    assert os.path.exists(f"{TESTFILE_PATH}/{TESTFILE_NAME}.txt")



def test_creation_of_second_file():
    """
    test creation of second file
    """
    create_test_file()
    assert os.path.exists(f"{TESTFILE_PATH}/{TESTFILE_NAME}1.txt")


def test_creation_of_third_file():
    """
    test creation of third file
    """
    create_test_file()
    assert os.path.exists(f"{TESTFILE_PATH}/{TESTFILE_NAME}2.txt")

#test iteration if file exists


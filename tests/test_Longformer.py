from sources import Longformer
from sources.Exceptions import TransformerNotInitializedException
import pytest

from . import SummaryTestingUtils

TEST_TEXT = SummaryTestingUtils.TEST_TEXT
TEST_SUMMARY = SummaryTestingUtils.LF_SUMMARY

@pytest.fixture(autouse=True)
def before_each_test():
    Longformer.teardown()

def test_setup():
    """
    Test that setup task initializes the model, tokenizer and sets the device
    """
    #test if setup has been run
    assert Longformer.isSetup == False
    assert Longformer.__model == None
    assert Longformer.__tokenizer == None

    Longformer.setup()

    assert Longformer.isSetup
    assert Longformer.__model != None
    assert Longformer.__tokenizer != None

def test_teardown():
    Longformer.setup()
    
    assert Longformer.isSetup == True

    Longformer.teardown()

    assert Longformer.isSetup == False
    assert Longformer.__model == None
    assert Longformer.__tokenizer == None

def test_summarization_without_setup():
    """
    Test that Transformer will not generate a result if it runs without setup
    """
    assert Longformer.isSetup == False
    with pytest.raises(TransformerNotInitializedException) as e_info:
        preprocess_text = TEST_TEXT.strip().replace("\n"," ")
        Longformer.create_summary(preprocess_text)   
        assert e_info.msg == "Transformer has not been setup"

def test_summarization_task():
    """
    Test summarization functionality of Transformer class
    """
    Longformer.setup()
    preprocess_text = TEST_TEXT.strip().replace("\n"," ")
    result = Longformer.create_summary(preprocess_text) 
    result = result.strip().replace("\n"," ") 
    assert result == TEST_SUMMARY
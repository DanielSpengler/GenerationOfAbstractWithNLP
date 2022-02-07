from sources import RoBERTa
from sources.Exceptions import TransformerNotInitializedException
import pytest

from . import SummaryTestingUtils

TEST_TEXT = SummaryTestingUtils.TEST_TEXT
TEST_SUMMARY = SummaryTestingUtils.RoBERTa_SUMMARY

@pytest.fixture(autouse=True)
def before_each_test():
    RoBERTa.teardown()

def test_setup():
    """
    Test that setup task initializes the model, tokenizer and sets the device
    """
    #test if setup has been run
    assert RoBERTa.isSetup == False
    assert RoBERTa.__model == None
    assert RoBERTa.__tokenizer == None

    RoBERTa.setup()

    assert RoBERTa.isSetup
    assert RoBERTa.__model != None
    assert RoBERTa.__tokenizer != None

def test_teardown():
    RoBERTa.setup()
    
    assert RoBERTa.isSetup == True

    RoBERTa.teardown()

    assert RoBERTa.isSetup == False
    assert RoBERTa.__model == None
    assert RoBERTa.__tokenizer == None

def test_summarization_without_setup():
    """
    Test that Transformer will not generate a result if it runs without setup
    """
    assert RoBERTa.isSetup == False
    with pytest.raises(TransformerNotInitializedException) as e_info:
        preprocess_text = TEST_TEXT.strip().replace("\n"," ")
        RoBERTa.create_summary(preprocess_text)   
        assert e_info.msg == "Transformer has not been setup"

def test_summarization_task():
    """
    Test summarization functionality of Transformer class
    """
    RoBERTa.setup()
    preprocess_text = TEST_TEXT.strip().replace("\n"," ")
    result = RoBERTa.create_summary(preprocess_text) 
    result = result.strip().replace("\n"," ") 
    assert result == TEST_SUMMARY
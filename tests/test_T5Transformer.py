import pytest

from . import SummaryTestingUtils
from sources import T5Transformer
from sources.Exceptions import TransformerNotInitializedException

TEST_TEXT = SummaryTestingUtils.TEST_TEXT
TEST_SUMMARY = SummaryTestingUtils.T5_SUMMARY

@pytest.fixture(autouse=True)
def before_each_test():
    T5Transformer.teardown()

def test_setup():
    """
    Test that setup task initializes the model, tokenizer and sets the device
    """
    #test if setup has been run
    assert T5Transformer.isSetup == False
    assert T5Transformer.__model == None
    assert T5Transformer.__tokenizer == None
    assert T5Transformer.__device == None

    T5Transformer.setup()

    assert T5Transformer.isSetup
    assert T5Transformer.__model != None
    assert T5Transformer.__tokenizer != None
    assert T5Transformer.__device != None

def test_teardown():
    T5Transformer.setup()
    
    assert T5Transformer.isSetup == True

    T5Transformer.teardown()

    assert T5Transformer.isSetup == False
    assert T5Transformer.__model == None
    assert T5Transformer.__tokenizer == None
    assert T5Transformer.__device == None

def test_summarization_without_setup():
    """
    Test that Transformer will not generate a result if it runs without setup
    """
    assert T5Transformer.isSetup == False
    with pytest.raises(TransformerNotInitializedException) as e_info:
        preprocess_text = TEST_TEXT.strip().replace("\n"," ")
        T5Transformer.create_summary(preprocess_text)   
        assert e_info.msg == "Transformer has not been setup"

def test_summarization_task():
    """
    Test summarization functionality of Transformer class
    """
    T5Transformer.setup()
    preprocess_text = TEST_TEXT.strip().replace("\n"," ")
    result = T5Transformer.create_summary(preprocess_text) 
    result = result.strip().replace("\n"," ")   
    assert result == TEST_SUMMARY
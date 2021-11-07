from sources import Transformer
from sources.Exceptions import TransformerNotInitializedException
import pytest

from . import SummaryTestingUtils

TEST_TEXT = SummaryTestingUtils.TEST_TEXT
TEST_SUMMARY = SummaryTestingUtils.T5_SUMMARY

@pytest.fixture(autouse=True)
def before_each_test():
    Transformer.teardown()

def test_setup():
    """
    Test that setup task initializes the model, tokenizer and sets the device
    """
    #test if setup has been run
    assert Transformer.isSetup == False
    assert Transformer.model == None
    assert Transformer.tokenizer == None
    assert Transformer.device == None

    Transformer.setup()

    assert Transformer.isSetup
    assert Transformer.model != None
    assert Transformer.tokenizer != None
    assert Transformer.device != None

def test_teardown():
    Transformer.setup()
    
    assert Transformer.isSetup == True

    Transformer.teardown()

    assert True

    assert Transformer.isSetup == False
    assert Transformer.model == None
    assert Transformer.tokenizer == None
    assert Transformer.device == None

def test_summarization_without_setup():
    """
    Test that Transformer will not generate a result if it runs without setup
    """
    assert Transformer.isSetup == False
    with pytest.raises(TransformerNotInitializedException) as e_info:
        preprocess_text = TEST_TEXT.strip().replace("\n"," ")
        Transformer.create_summary(preprocess_text)   
        assert e_info.msg == "Transformer has not been setup"

def test_summarization_task():
    """
    Test summarization functionality of Transformer class
    """
    Transformer.setup()
    preprocess_text = TEST_TEXT.strip().replace("\n"," ")
    result = Transformer.create_summary(preprocess_text)    
    assert result == TEST_SUMMARY
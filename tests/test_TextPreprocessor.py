from sources import TextPreprocessor


TEST_TEXT = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat"

def test_remove_whitespaces():
    """
    Test if leading and trailing spaces are removed
    """
    to_clean = " " + TEST_TEXT + "   "
    cleaned = TextPreprocessor.remove_leading_trailing_whitespaces(to_clean)
    assert cleaned == TEST_TEXT

def test_remove_before_introduction():
    """
    Test if text before the keyword 'INTRODUCTION' is removed
    """
    expected = "INTRODUCTION" + " " + TEST_TEXT
    to_clean = "This is a test " + expected
    cleaned = TextPreprocessor.remove_text_before_introduction(to_clean)
    assert cleaned == expected

def test_remove_references():
    """
    Test if text afer keyword 'REFERENCES' is removed
    """
    expected = TEST_TEXT + " "
    to_clean = expected + "REFERENCES This is a Test..."
    cleaned = TextPreprocessor.remove_text_after_references(to_clean)
    assert cleaned == expected

def test_remove_linebreaks():
    """
    Test if linebreaks are removed
    """
    expected = TEST_TEXT
    to_clean = TEST_TEXT.replace(', ', ',\n') 
    cleaned = TextPreprocessor.remove_linebreaks(to_clean)
    assert cleaned == expected

def test_complete_preprocessing():
    """
    Test whole integration of all sub-processings
    """
    expected = "INTRODUCTION" + " " + TEST_TEXT
    to_clean = expected
    #add linebreaks after each comma
    to_clean = to_clean.replace(', ', ',\n') 
    #add leading and trailing whitespaces to 'inner' text body
    to_clean = " " + to_clean + "   "
    #add text before the Introdcution
    to_clean = "This is a test " + " " + to_clean
    #add References
    to_clean = to_clean + "REFERENCES This is a Test..."
    #clean up the text
    cleaned = TextPreprocessor.preprocess_text(to_clean)
    assert cleaned == expected

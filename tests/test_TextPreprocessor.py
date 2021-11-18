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
    
def test_remove_authorization_note():
    """
    Test if non-unicode characters are removed
    """
    expected = TEST_TEXT + " " + "END"
    authorization_note = "Authorized licensed use limited to: FOM University of Applied Sciences. Downloaded on January 13,2021 at 19:41:19 UTC from IEEE Xplore.  Restrictions apply."
    to_clean = TEST_TEXT + authorization_note + "END"
    cleaned = TextPreprocessor.remove_authorization_note(to_clean)
    assert cleaned == expected

def test_remove_non_unicode_characters():
    """
    Test if non-unicode characters are removed
    """
    expected = TEST_TEXT
    to_clean = "(cid:22) (cid:1) (cid:234)" + expected + "(cid:22) (cid:1) (cid:234)"
    cleaned = TextPreprocessor.remove_non_unicode_characters(to_clean)
    cleaned = cleaned.strip()
    assert cleaned == expected

def test_remove_linebreaks():
    """
    Test if linebreaks are removed
    """
    expected = TEST_TEXT
    to_clean = TEST_TEXT.replace(', ', ',\n') 
    cleaned = TextPreprocessor.remove_linebreaks(to_clean)
    assert cleaned == expected

def test_remove_double_spaces():
    """
    Test if double spaces within the text will be removed
    """
    to_clean = TEST_TEXT.replace(',', ', ') 
    cleaned = TextPreprocessor.remove_double_spaces(to_clean)
    assert cleaned == TEST_TEXT
    #test triple spaces
    to_clean = TEST_TEXT.replace(',', ',   ') 
    cleaned = TextPreprocessor.remove_double_spaces(to_clean)
    assert cleaned == TEST_TEXT

def test_complete_preprocessing():
    """
    Test whole integration of all sub-processings
    """
    expected = "INTRODUCTION" + " " + TEST_TEXT
    to_clean = expected
    #add multiple whitespaces
    to_clean = to_clean.replace(',', ',  ') 
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

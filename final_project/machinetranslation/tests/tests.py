from translator import englishToFrench, frenchToEnglish

# Test englishToFrench
def test_englishToFrench():
    # Test case: Null input
    assert englishToFrench("") == ""
    # Test case
    assert englishToFrench("Hello") == "Bonjour"


# Test frenchToEnglish
def test_frenchToEnglish():
    # Test case: Null input
    assert frenchToEnglish("") == ""
    # Test case
    assert frenchToEnglish("Bonjour") == "Hello"

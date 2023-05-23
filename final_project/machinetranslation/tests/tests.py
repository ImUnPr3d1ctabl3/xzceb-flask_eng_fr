import unittest
from translator import english_to_french, french_to_english

# Test englishToFrench
def test_english_to_french():
    assertEqual(english_to_french('Hello'), 'Bonjour')
    assertNotEqual(english_to_french('Goodbye'), 'Au revoir')


# Test frenchToEnglish
def test_french_to_english():
    assertEqual(french_to_english('Bonjour'), 'Hello')
    assertNotEqual(french_to_english('Au revoir'), 'Goodbye')

if __name__ == '__main__':
    unittest.main()
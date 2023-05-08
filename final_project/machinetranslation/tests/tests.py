import unittest
from ..translator import english_to_french, french_to_english


class TestMyModule(unittest.TestCase):
    def test_en_to_fr(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # Test if 'Hello' returns 'Bonjour'
        self.assertIsNotNone(english_to_french('Sample Text'), True)  # Test for the null inputs
        self.assertNotEqual(english_to_french('Hello'), 'Hello')  # Assert_Not_Equal

    def test_fr_to_en(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # Test if 'Bonjour' returns 'Hello'
        self.assertIsNotNone(french_to_english('Sample Text'), True)  # Test for the null inputs
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')  # Assert_Not_Equal


unittest.main()

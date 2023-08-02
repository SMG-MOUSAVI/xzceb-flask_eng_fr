from translator import english_to_french, french_to_english
import unittest

class TestTranslator(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')

    def test_englishNToFrench(self):
        self.assertNotEqual(english_to_french('bye'),'Bonjour')

    def test_frenchNToEnglish(self):
        self.assertNotEqual(french_to_english('Bonjour'),'bye')

if __name__ == '__main__':
    unittest.main()

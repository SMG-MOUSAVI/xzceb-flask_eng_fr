''' hi '''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    ''' hey'''
    french_text = MyMemoryTranslator(source='en-GB', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    ''' hey'''
    english_text = MyMemoryTranslator(source='f-r-FR', target='english').translate(french_text)
    return english_text
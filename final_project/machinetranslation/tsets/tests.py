from translator import english_to_french, french_to_english

def test_englishToFrench():
    assert english_to_french('Hello') == 'Bonjour'

def test_frenchToEnglish():
    assert french_to_english('Bonjour') == 'Hello'

test_englishToFrench()
test_frenchToEnglish()

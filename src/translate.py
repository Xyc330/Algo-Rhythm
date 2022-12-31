from googletrans import Translator


# TRANSLATOR
def translate(text, dest='ru'):
    translator = Translator()
    return translator.translate(text, dest=dest).text


def detectLang(text):
    # known bugs
    if text.lower() in ['ik', 'noice']:
        return 'en'

    translator = Translator()

    detection = translator.detect(text)
    lang = 'en'
    if detection.confidence >= 0.8:
        lang = detection.lang

    return lang

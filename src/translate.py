from googletrans import Translator


# TRANSLATOR
def translate(text, dest='ru'):
    translator = Translator()
    return translator.translate(text, dest=dest).text


def detectLang(text):
    # known bugs
    if text.lower() in ['ik', 'noice', 'bruv']:
        return 'en'

    translator = Translator()

    detection = translator.detect(text)
    lang = 'en'
    confidence_threshold = 0.9
    if str(type(detection.confidence)) == '<class \'list\'>':
        if detection.confidence[0] >= confidence_threshold:
            lang = detection.lang
    elif detection.confidence >= confidence_threshold:
        lang = detection.lang

    return lang


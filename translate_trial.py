from googletrans import Translator

translator = Translator()
translated = translator.translate("中文", dest='en')
print(translated)
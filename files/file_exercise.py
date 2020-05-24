# building a translator
from translate import  Translator

translator = Translator(to_lang="ja")
text = ''


try:
    with open('translation_file.txt', 'r') as f:
        text = f.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print("file Not found")

try:
    with open('translated_file.txt', 'w') as f:
        f.write(translation)
except FileExistsError as err:
    raise err
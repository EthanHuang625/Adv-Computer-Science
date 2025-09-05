import subprocess

class Translator:
    """
    Translator using translate-shell (trans) command line tool.
    """
    def __init__(self):
        pass

    def translate(self, text, to_lang, from_lang=None):
        """
        Translate text using translate-shell.
        Parameters:
            text (str): Text to translate
            to_lang (str): Target language code
            from_lang (str, optional): Source language code
        Returns:
            str: Translated text
        """
        cmd = ["trans", "-b"]
        if from_lang:
            cmd.append(f"{from_lang}:{to_lang}")
        else:
            cmd.append(to_lang)
        cmd.append(text)
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()

name = input ("Name: ")
age = int(input ("Age: "))
languages_yes = input ("Do you speak any other languages? ")
if languages_yes.lower() == "yes":
    language = input ("What other language do you speak? ")
else:
    language = "None"

user = {
    "name": name,
    "age": age,
    "languages": language
}

translator = Translator()

intro_text = f"Hello, {user['name']}! You are {user['age']} years old and you speak {user['languages']}"

if language != "None":
    intro_translation = translator.translate(intro_text, language)
    print(f"Introduction in {language}: {intro_translation}")
else:
    intro_translation = translator.translate(intro_text, "zh-CN")
    print(f"Introduction in Chinese: {intro_translation}")

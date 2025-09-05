import subprocess

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

def translate_text(text, to_lang, from_lang=None):
    """
    Use translate-shell (trans) to translate text.
    """
    cmd = ["trans", "-b"]
    if from_lang:
        cmd.append(f"{from_lang}:{to_lang}")
    else:
        cmd.append(to_lang)
    cmd.append(text)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

# Translate 'Hello, how are you?' to Chinese
translation_ch = translate_text("Hello, how are you?", "zh-CN")
print(f"Chinese translation: {translation_ch}")

# Translate '안녕하세요.' (Korean) to English
translation_en = translate_text("안녕하세요.", "en", from_lang="ko")
print(f"English translation: {translation_en}")
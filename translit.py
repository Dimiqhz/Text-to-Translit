import json

russian_to_translit = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
    'е': 'e', 'ё': 'yo','ж': 'zh','з': 'z', 'и': 'i',
    'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
    'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'kh','ц': 'ts','ч': 'ch',
    'ш': 'sh','щ': 'shch','ъ': '',  'ы': 'y', 'ь': '',
    'э': 'e','ю': 'yu','я': 'ya'
}

def load_translations():
    with open("translations.json", "r", encoding="utf-8") as file:
        return json.load(file)

def transliterate(text, replace_spaces):
    result = []
    for char in text:
        lower_char = char.lower()
        if lower_char in russian_to_translit:
            translit_char = russian_to_translit[lower_char]
            if char.isupper():
                translit_char = translit_char.capitalize()
            result.append(translit_char)
        elif char == ' ' and replace_spaces:
            result.append('-')
        else:
            result.append(char)
    return "".join(result)

def main():
    translations = load_translations()

    lang_choice = input("Choose language / Выберите язык (en/ru): ").strip().lower()
    if lang_choice not in ["en", "ru"]:
        print("Invalid choice / Некорректный выбор.")
        return

    lang = translations[lang_choice]

    print(lang["choose_option"])
    print(lang["manual_input_option"])
    print(lang["file_input_option"])
    choice = input(lang["your_choice"]).strip()

    replace_spaces = input(lang["replace_spaces"]).strip().lower() == lang["yes"]

    if choice == "1":
        user_text = input(lang["enter_text"]) 
        print(lang["result"])
        print(transliterate(user_text, replace_spaces))
    elif choice == "2":
        try:
            with open("input.txt", "r", encoding="utf-8") as infile:
                file_content = infile.read()
            transliterated_content = transliterate(file_content, replace_spaces)
            with open("output.txt", "w", encoding="utf-8") as outfile:
                outfile.write(transliterated_content)
            print(lang["file_result"])
        except FileNotFoundError:
            print(lang["file_not_found"])
    else:
        print(lang["invalid_choice"])

if __name__ == "__main__":
    main()

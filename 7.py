import re


def remove_text_in_brackets(text):
    return re.sub(r'\([^)]*\)', '', text)


if __name__ == '__main__':
    text = input('Введите строку: ')
    new_text = remove_text_in_brackets(text)
    new_text = re.sub(r'\s{2,}', ' ', new_text)  # Заменяем > 2 пробелов на 1
    print(new_text)

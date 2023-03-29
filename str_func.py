def return_big_letter(text):
    """
    функция делает заглавной каждую букву слова
    :param text:
    :return: строку
    """
    return text.upper()

def return_word_first_letter(text):
    """
    функция делает заглавной первую букву слова в строке
    :param text:
    :return: строку где каждое слово начинаетсмя с заглавной буквы
    """
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

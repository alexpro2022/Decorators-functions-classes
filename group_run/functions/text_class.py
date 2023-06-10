"""
E. Написать класс, принимающий на вход текст. Один метод класса должен
   выводить в консоль самое длинное слово в тексте. Второй метод - самое
   часто встречающееся слово. Третий метод выводит количество спецсимволов
   в тексте (точки, запятые и так далее). Четвертый метод выводит все
   палиндромы через запятую.
F. Написать декоратор к предыдущему классу, который будет выводить в консоль
   время выполнения каждого метода. Результат выполнения задания должен быть
   оформлен в виде файла с кодом.

"""


import string as s
import time


def timer(func):
    MSG = '\nВремя выполнения функции "{}" составило {:.5f} секунд.'

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(MSG.format(func.__name__, time.time() - start_time))
        return result
    return wrapper


class Text:
    RUS_ALPHABET = ''.join([chr(i) for i in range(ord('А'), ord('я') + 1)])
    ALPHABET = RUS_ALPHABET + s.ascii_letters + s.digits
    LONGEST_WORD_MSG = 'Самое длинное слово в тексте: "{}".'
    FREQUENT_WORD_MSG = 'Самое часто встречающееся слово: "{}".'
    SPECIAL_SIMBOLS_MSG = ('Количество спецсимволов в тексте '
                           '(точки, запятые и т. д.): {}.')
    PALINDROMES_MSG = ('Все палиндромы:\n  '
                       '*слова - {}\n  '
                       '*предложения:\n   | {}')

    def __init__(self, text: str) -> None:
        self.text = text

    def __get_words(self, min_length: int = 1):
        """Возвращает из текста все слова указанной длины (символов)."""
        min_length = 1 if min_length < 1 else min_length
        words, word = [], []
        for char in self.text:
            if char in set(self.ALPHABET + '-' + '_'):
                word.append(char)
            else:
                if len(word) >= min_length:
                    words.append(''.join(word))
                word.clear()
        return words

    def __get_sentences(self, min_length: int = 2):
        """Возвращает из текста все предложения указанной длины (слов).
           Предложения - фрагменты текста оканчивающиеся на символы '.!?'.
           Удаляет из предложения знаки переноса строки."""
        min_length = 1 if min_length < 1 else min_length
        sentences, sentence = [], []
        for char in self.text:
            if char not in ('.', '!', '?'):
                (sentence.append(char) if char != '\n'
                 else sentence.append(' '))
            else:
                s = ''.join(sentence).strip()
                if len(s.split()) >= min_length:
                    sentences.append(s)
                sentence.clear()
        return sentences

    def __is_palindrome(self, item: str):
        s = [char.lower() for char in item if char in set(self.ALPHABET)]
        return s == s[::-1]

    @timer
    def longest_word(self):
        return self.LONGEST_WORD_MSG.format(
            max(self.__get_words(), key=lambda x: len(x)))

    @timer
    def frequent_word(self, min_length: int = 2):
        words = self.__get_words(min_length)
        unique_words = set(words)
        counter = {}
        for word in unique_words:
            counter[words.count(word)] = word
        return self.FREQUENT_WORD_MSG.format(counter[sorted(counter)[-1]])

    @timer
    def special_simbols_counter(self):
        counter = 0
        for char in self.text:
            if char not in set(self.ALPHABET + ' '):
                counter += 1
        return self.SPECIAL_SIMBOLS_MSG.format(counter)

    @timer
    def palindromes(self, min_length: int = 2):
        words = [word for word in self.__get_words(min_length)
                 if self.__is_palindrome(word)]
        sentences = [sentence for sentence in self.__get_sentences()
                     if self.__is_palindrome(sentence)]
        return self.PALINDROMES_MSG.format(', '.join(words),
                                           '\n   | '.join(sentences))


if __name__ == '__main__':

    def _get_test_data():
        with open('data.txt', encoding='utf-8') as f:
            return f.read()

    text = Text(_get_test_data())
    print(text.longest_word())
    print(text.frequent_word(min_length=5))
    print(text.special_simbols_counter())
    print(text.palindromes())

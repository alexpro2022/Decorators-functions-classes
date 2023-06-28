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
import os
import sys

if __package__:
    from . import decorators
else:
    sys.path.append(os.path.dirname(__file__) + '/.')
    import decorators

TEST_FILE_PATH = 'functions/data.txt'
ENCODING = 'utf-8'


@decorators.input
def __get_test_data():
    with open(TEST_FILE_PATH, encoding=ENCODING) as f:
        return f.read()


@decorators.timer_all_public_methods
class Text:
    RUS_ALPHABET = ''.join([chr(i) for i in range(ord('А'), ord('я') + 1)])
    ALPHABET = RUS_ALPHABET + s.ascii_letters + s.digits
    LONGEST_WORD_MSG = 'Самое длинное слово в тексте: "{}".'
    FREQUENT_WORD_MSG = 'Самое часто встречающееся слово из {} букв: "{}".'
    SPECIAL_SIMBOLS_MSG = ('Количество спецсимволов в тексте '
                           '(точки, запятые и т. д.): {}.')
    PALINDROMES_MSG = ('Все палиндромы:\n  '
                       '*слова - {}\n  '
                       '*предложения:\n   | {}.\n')

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

    @decorators.output
    def longest_word(self):
        return self.LONGEST_WORD_MSG.format(
            max(self.__get_words(), key=lambda x: len(x)))

    @decorators.output
    def frequent_word(self, min_length: int = 2):
        words = self.__get_words(min_length)
        unique_words = set(words)
        counter = {}
        for word in unique_words:
            counter[words.count(word)] = word
        return self.FREQUENT_WORD_MSG.format(min_length, counter[sorted(counter)[-1]])
    
    @decorators.output
    def special_simbols_counter(self):
        counter = 0
        for char in self.text:
            if char not in set(self.ALPHABET + ' '):
                counter += 1
        return self.SPECIAL_SIMBOLS_MSG.format(counter)

    @decorators.output
    def palindromes(self, min_length: int = 2):
        words = [word for word in self.__get_words(min_length)
                 if self.__is_palindrome(word)]
        sentences = [sentence for sentence in self.__get_sentences()
                     if self.__is_palindrome(sentence)]
        return self.PALINDROMES_MSG.format(', '.join(words),
                                           '\n   | '.join(sentences))


@decorators.timer
@decorators.output(title=__doc__)
def main():
    text = Text(__get_test_data())
    text.longest_word()
    text.frequent_word(min_length=5)
    text.special_simbols_counter()
    text.palindromes()    


if __name__ == '__main__':
    main()

import random
from valid_hangman_words import words


def pick_up_word(lst_words):
    """Pick up random word from words poll"""
    len_lst = len(lst_words)
    rnd_word_index = random.randint(0, len_lst - 1)
    return lst_words[rnd_word_index]


def display_word(word: str):
    """Print random word for player"""
    first = word[0:1]
    last = word[len(word) - 1:len(word)]
    middle_part = (word.lstrip(first)).rstrip(last)
    new_word = ''
    for chafr in middle_part:
        if chafr.isalpha():
            new_word = new_word + ' _ '
    return f'{first}{new_word}{last}'


def middle_part(word: str):
    first = word[0:1]
    last = word[len(word) - 1:len(word)]
    mid_part = (word.lstrip(first)).rstrip(last)

    return mid_part


def guessing_char(word: str):
    text = ''
    for char in word:
        if char.isalpha():
            text = text + ' _ '

    char = input('Please enter char: ')
    if char in word:


        pass


# print(display_word(pick_up_word(words)))
print(middle_part(pick_up_word(words)))
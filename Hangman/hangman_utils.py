import random
from valid_hangman_words import words


def pick_up_word():
    """Pick up random word from words poll"""
    len_lst = len(words)
    rnd_word_index = random.randint(0, len_lst - 1)
    return words[rnd_word_index]


def create_word_parts(word: str):
    """Create two word parts: first and last letter and middle part"""
    first = word[0:1]
    last = word[len(word) - 1:len(word)]
    mid_part = (word.lstrip(first)).rstrip(last)
    first_last = word.replace(mid_part, ' _ ' * len(mid_part))

    return first_last, mid_part


def player_input():
    player_letter = input('Please enter letter: ')

    return player_letter


def game():
    main_word = pick_up_word()
    word_parts = create_word_parts(main_word)

    first_last_letter = word_parts[0]  # l _  _  _  _ p
    mid_letters = word_parts[1]  # apto
    shadow = '*' * len(mid_letters)

    while True:
        print(first_last_letter)
        my_dict = {}  # {0: 'h', 1: 'a', 2: 'i'}
        lst_shadow = list(shadow)

        for count, value in enumerate(mid_letters):
            my_dict[count] = value

        lst_keys = list(my_dict.keys())
        lst_values = list(my_dict.values())

        player_char = player_input()

        if player_char in lst_values:
            char_index = lst_values.index(player_char)
            char = lst_values[char_index]
            lst_shadow[char_index] = char
            print(lst_shadow)
        else:
            print("Wrong letter")

        if "*" not in lst_shadow:
            break


game()

# def word_after_correct_guessed_char(word: str, char):
#     display_w = ''
#     for i in word:
#         if i == char:
#             display_w = f"{display_w} {char} "
#         else:
#             display_w = display_w + ' _ '
#
#     return display_w
#
#
# def guessing_char(word: str):
#     print(word)
#     text = ''
#     for char in word:
#         if char.isalpha():
#             text = text + ' _ '
#
#     # This dic contain word middle part
#     mid_part = middle_part(word)
#     my_dict = {}  # {0: 'h', 1: 'a', 2: 'i'}
#
#     print(f'Mid part: {mid_part}')
#     for count, value in enumerate(mid_part):
#         my_dict[count] = value
#
#     print(my_dict)
#     char = input('Please enter char: ')
#
#     lst_key = list(my_dict.keys())
#     lst_values = list(my_dict.values())
#
#     guessed_letter = ''
#
#     if char in lst_values:
#         c_index = lst_values.index(char)
#         guessed_letter = lst_key.index(c_index)
#         print(word_after_correct_guessed_char(word, guessed_letter))
#
#     else:
#         print('Wrong char')
#
#
#
#
# # print(display_word(pick_up_word(words)))
# # print(middle_part(pick_up_word(words)))
# guessing_char(pick_up_word(words))

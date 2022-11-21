import random
from valid_hangman_words import words
from visual_parts import parts


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
    first_last = word.replace(mid_part, '*' * len(mid_part))

    return first_last, mid_part


def player_input():
    """Receive player letter"""
    player_letter = input('Please enter letter: ')

    return player_letter


def play_again():
    player_choice = input("Play again? (y/n):\n")
    if player_choice == 'y':
        game()
    else:
        pass


def game():
    main_word = pick_up_word()
    word_parts = create_word_parts(main_word)

    first_last_letter = word_parts[0]
    mid_letters = word_parts[1]

    # Replace mid-letters with symbols
    shadow = '*' * len(mid_letters)

    # Create lists with letters and symbols
    lst_shadow = list(shadow)
    lst_first_last_letter = list(first_last_letter)

    playing = True
    wrong_letter_cnt = 0
    player_letter_lst = []

    while playing:
        print(f"Player guessed letters: {player_letter_lst}")
        print('# '*20)
        display_word = ''
        for char in lst_first_last_letter:
            display_word = display_word + char

        print(f"Guess the word:\n{display_word}")

        # Dict contains mid letters
        my_dict = {}

        for count, value in enumerate(mid_letters):
            my_dict[count] = value

        lst_values = list(my_dict.values())

        player_char = player_input()

        if player_char in lst_values:
            print(f"You guessed the letter '{player_char}'")
            char_index = lst_values.index(player_char)
            char = lst_values[char_index]
            lst_shadow[char_index] = char
            lst_first_last_letter[char_index + 1] = char

        else:
            print(f"Wrong letter '{player_char}'. Try Again!")
            player_letter_lst.append(player_char)
            wrong_letter_cnt += 1
            print(parts[wrong_letter_cnt-1])

            if wrong_letter_cnt == 8:
                print('You are hanged!!! Game over.')

                # TODO: Create property code here

        if "*" not in lst_shadow:
            print(f'You won! The word is: {main_word.upper()}')

            play_again()
            playing = False
            break



from valid_words import valid_words
import random

CHOSEN_WORD = random.choice(valid_words)
GUESSES_COUNT = 7


class GuessWord:
    counter = 1

    def __init__(self, w_str: str):
        self.w_str = w_str
        self.w_chars = list(self.w_str)

    def jump_turn(self):
        GuessWord.counter += 1

    def is_valid(self):
        return self.w_str in valid_words


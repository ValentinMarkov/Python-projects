
# правим дикт от което на рандом примцип взимаме една к, v двойка. После още една и питаме играча коя според него е по-търсена
"""
dict_questions = {'red hot chili paper': 250 000, 'metallica': 350 000, 'Paris': 703 000, 'london': 450 000,
 'scarlet johanson': 389 000, 'the rock':790 000}
"""
# The player input the answer. Compare answer tо element value, If win delete this element fromn dic, pick up randomn new element and compare
# give +1 to player score
# if player lose quit game --> give some random title and print score
from random import random

from helper import lst_questions


def pick_rnd_element(source:list):
    return source.index(2)



print(pick_rnd_element(lst_questions))

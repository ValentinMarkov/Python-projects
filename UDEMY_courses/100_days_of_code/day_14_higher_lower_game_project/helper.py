import os
import random


def get_rnd_element(source: list):
    """Return random dictionary"""
    rnd_index = random.randint(0, len(source) - 1)
    return source[rnd_index], rnd_index


def remove_already_picked_element(source: list, picked_element: int):
    source = source.pop(picked_element)
    return source


def get_and_remove_one_element(source):
    first = get_rnd_element(source)  # ({'London': 450000}, 4)
    remove_already_picked_element(source, first[1])

    data = ()

    for k, v in first[0].items():
        data = k, v

    return data


def game(source: list):
    flag = True

    player_score = 0
    first_element_to_compare = 0

    while True:
        if flag:
            if len(source) == 0:
                print('No more item in DB')
                break

            one = get_and_remove_one_element(source)
            two = get_and_remove_one_element(source)

            print(f"More searches for {one[0]} witch {one[1]} searches, or for {two[0]}?")
            player_answer = int(input(f'Select {one[0]}-(1) or {two[0]}-(2)? \n'))
            os.system('cls')

            if one[1] > two[1]:
                correct_answer = 1
                first_element_to_compare = two
                answer_key = one[0]
                answer_value = one[1]
                loser_key = two[0]
                loser_value = two[1]

            else:
                correct_answer = 2
                first_element_to_compare = two  # ('London', 450000)
                answer_key = two[0]
                answer_value = two[1]
                loser_key = one[0]
                loser_value = one[1]

            if correct_answer == player_answer:
                player_score += 1
                print('\nCorrect !!!')
                print(f'Player score: {player_score} points')
                print(
                    f"{answer_key} witch {answer_value} searches VS {loser_key} witch {loser_value} searches\n")

            else:
                print('Wrong !!!')
                print(
                    f"{answer_key} witch {answer_value} searches VS {loser_key} witch {loser_value} searches")
                print(f'Player score: {player_score} points')
                break

            flag = False

        else:
            if len(source) == 0:
                print('No more item in DB. Game ends ;-(')
                break

            first = first_element_to_compare
            two = get_and_remove_one_element(source)

            print(f"More searches for {first[0]} witch {first[1]} searches, or for {two[0]}?")
            player_answer = int(input(f'Select {first[0]}-(1) or {two[0]}-(2)? \n'))
            os.system('cls')

            if first[1] > two[1]:
                correct_answer = 1
                first_element_to_compare = two
                answer_key = first[0]
                answer_value = first[1]
                loser_key = two[0]
                loser_value = two[1]

            else:
                correct_answer = 2
                first_element_to_compare = two
                answer_key = two[0]
                answer_value = two[1]
                loser_key = first[0]
                loser_value = first[1]

            if correct_answer == player_answer:
                player_score += 1
                print('\nCorrect !!!')
                print(f'Player score: {player_score} points')
                print(
                    f"{answer_key} witch {answer_value} searches VS {loser_key} witch {loser_value} searches\n")

            else:
                print('Wrong !!!')
                print(
                    f"{answer_key} witch {answer_value} searches VS {loser_key} witch {loser_value} searches")
                print(f'Player score: {player_score} points')
                break



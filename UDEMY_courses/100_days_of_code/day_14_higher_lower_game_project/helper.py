import random

lst_questions = [{'red hot chili paper': 250000}, {'everest': 550000}, {'japan': 1000000},
                 {'metallica': 350000},
                 {'Paris': 703000},
                 {'London': 450000},
                 {'Scarlet Johanson': 389000},
                 {'the Rock': 790000}]


def get_rnd_element(source: list):
    """Return random dictionary"""
    rnd_index = random.randint(0, len(source) - 1)
    return source[rnd_index], rnd_index


def remove_already_picked_element(source: list, picked_element: int):
    source = source.pop(picked_element)
    return source


def get_and_remove_two_elements(source):
    first = get_rnd_element(source)  # ({'London': 450000}, 4)
    remove_already_picked_element(source, first[1])

    second = get_rnd_element(source)
    remove_already_picked_element(source, second[1])

    my_key_first = [k for k, v in first[0].items()]
    my_value_first = [v for k, v in first[0].items()]

    my_key_second = [k for k, v in second[0].items()]
    my_value_second = [v for k, v in second[0].items()]

    return my_key_first, my_value_first, my_key_second, my_value_second


def get_and_remove_one_element(source):
    first = get_rnd_element(source)  # ({'London': 450000}, 4)
    remove_already_picked_element(source, first[1])

    # my_key_first = [k for k, v in first[0].items()]
    # my_value_first = [v for k, v in first[0].items()]

    # return my_key_first, my_value_first
    return first[0]



def game(source: list):
    flag = True

    correct_answer = 0
    player_score = 0
    first_element_to_compare = 0

    while True:
        if flag:
            if len(source) == 0:
                print('No more item in DB')
                break

            two_elements = get_and_remove_two_elements(source)  # return my_key_first, my_value_first, my_key_second, my_value_second
            # (['the Rock'], [790000], ['London'], [450000])

            print(f"More searches for '{two_elements[0][0]}' witch {two_elements[1][0]} searches, or for '{two_elements[2][0]}'?")
            player_answer = int(input(f'Select "{two_elements[0][0]}" or "{two_elements[2][0]}"? Answer 1 or 2: '))

            if two_elements[1][0] > two_elements[3][0]:
                correct_answer = 1
                first_element_to_compare = (two_elements[0], two_elements[1])

            else:
                correct_answer = 2
                first_element_to_compare = first_element_to_compare = (two_elements[2], two_elements[3])

            if correct_answer == player_answer:
                player_score += 1
                print('Correct !!!')
                print(f'Player score: {player_score} points')
                print(
                    f"'{two_elements[0][0]}' witch {two_elements[1][0]} searches VS '{two_elements[2][0]}' witch {two_elements[3][0]} searches")
            else:
                print('Wrong !!!')
                print(
                    f"'{two_elements[0][0]}' witch {two_elements[1][0]} searches VS '{two_elements[2][0]}' witch {two_elements[3][0]} searches")
                print(f'Player score: {player_score} points')
                break

            flag = False

        else:
            if len(source) == 0:
                print('No more item in DB')
                break

            first = first_element_to_compare

            second = get_and_remove_one_element(source)

            print(
                f"More searches for '{first[0]}' witch {first[1]} searches, or for '{second[0]}'?")
            player_answer = int(input(f'Select "{first[0]}" or "{second[0]}"? Answer 1 or 2: '))

            correct_answer = 0
            player_score = 0
            if first[0][1] > second[3][0]:
                correct_answer = 1
            else:
                correct_answer = 2

            if correct_answer == player_answer:
                player_score += 1
                print('Correct !!!')
                print(f'Player score: {player_score} points')
                print(
                    f"'{first[0]}' witch {first[1]} searches VS '{second[0]}' witch {second[1]} searches")

                first_element_to_compare = second

            else:
                print('Wrong !!!')
                print(
                    f"'{first[0][0]}' witch {first[0][1]} searches VS '{second[0][0]}' witch {second[3][0]} searches")
                print(f'Player score: {player_score} points')
                break



game(lst_questions)


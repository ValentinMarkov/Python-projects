from random import randint


def create_game_number(start_num=0, end_number=10):
    """Create random game number"""
    return randint(start_num, end_number)


def player_input():
    player_number = int(input("Player, your guessing number is: -->"))

    return player_number


def game_hint(number, stage):
    if stage == 0:
        if number > 5:
            print('Wrong Number!\nThe number is greater than 5')
        else:
            print('Wrong Number!\nThe number is smaller than 6')

    elif stage == 1:
        if number in list(range(1, 6)):
            if number in [1, 2, 3]:
                print('The number is 1, 2 or 3')
            else:
                print('The number is 4 or 6')

        else:
            if number in [6, 7, 8]:
                print('The number is 6, 7 or 8')
            else:
                print('The number is 9 or 10')


def play_number_guessing():
    number = create_game_number()
    game = True
    hint_stage = 0

    while game:
        print('Guess number between 0 and 10')
        player_number = player_input()

        if player_number == number:
            print(f"You WIN !!! You guess number {player_number}.")
            game = False
            break

        else:
            game_hint(number, hint_stage)
            hint_stage += 1

            if hint_stage > 3:
                print('Too many hints!. You lose game !!!')
                game = False
                break

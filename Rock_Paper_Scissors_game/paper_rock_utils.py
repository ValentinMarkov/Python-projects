from random import randint


def player_move():
    item = input("Pick up: Rock (r), Scissors (s) or Paper (p):  ")

    return item


def computer_move():
    dict_item = {1: 'r', 2: 's', 3: 'p'}
    item = randint(1, 3)

    return dict_item[item]


def play_game():
    player_item = player_move()
    com_move = computer_move()
    s, r, p = 'Scissor', 'ROCK', 'Paper'
    equality = 'There is no winner. Play again!'
    pl_win = 'Player WIN !!!'
    pl_lose = 'Player LOSE !!!'

    if player_item == 'r' and com_move == 's':
        print(f"Player {r} vs Computer {s}. {pl_win}")

    elif player_item == 'r' and com_move == 'r':
        print(f'Player {r} vs Computer {r}. {equality}')
        play_game()

    elif player_item == 'r' and com_move == 'p':
        print(f'Player {r} vs Computer {p}. {pl_lose}')

    elif player_item == 's' and com_move == 's':
        print(f'Player {s} vs Computer {s}. {equality}')
        play_game()

    elif player_item == 's' and com_move == 'r':
        print(f'Player {s} vs Computer {r}. {pl_lose}')

    elif player_item == 's' and com_move == 'p':
        print(f'Player {s} vs Computer {p}. {pl_win}')

    elif player_item == 'p' and com_move == 's':
        print(f'Player {p} vs Computer {s}. {pl_lose}')

    elif player_item == 'p' and com_move == 'r':
        print(f'Player {p} vs Computer {r}. {pl_win}')

    elif player_item == 'p' and com_move == 'p':
        print(f'Player {p} vs Computer {p}. {equality}')
        play_game()



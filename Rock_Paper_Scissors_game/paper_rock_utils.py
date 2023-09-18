from random import randint


def player_move():
    item = input("Pick up: Rock (r), Scissors (s) or Paper (p):  ")

    return item


def computer_move():
    dict_item = {1: 'r', 2: 's', 3: 'p'}
    item = randint(1, 3)

    return dict_item[item]


def win_counter(game_results):
    if game_results[0] > game_results[1]:
        result = f'The winner is PLAYER with result: {game_results[0]} vs {game_results[1]}'
    else:
        result = f'The winner is Computer with result: {game_results[1]} vs {game_results[0]}'

    return result


def play_game():
    s, r, p = 'Scissor', 'Rock', 'Paper'
    pl_win = 'Player WIN !!!'
    pl_lose = 'Player LOSE !!!'

    pl_win_cnt = 0
    com_win_cnt = 0

    while pl_win_cnt or com_win_cnt < 3:
        player_move()
        computer_move()
        print(player_move())
        print(computer_move())

        if player_move() == computer_move():
            print(f'EQUALITY: {player_move()} vs {computer_move()}')

        elif player_move() == 'r' and computer_move() == 'p':
            com_win_cnt += 1
            print(f'Player {r} vs Computer {p}. {pl_lose}')

        elif player_move() == 's' and computer_move() == 'r':
            com_win_cnt += 1
            print(f'Player {s} vs Computer {r}. {pl_lose}')

        elif player_move() == 's' and computer_move() == 'p':
            pl_win_cnt += 1
            print(f'Player {s} vs Computer {p}. {pl_win}')

        elif player_move() == 'p' and computer_move() == 's':
            pl_win_cnt += 1
            print(f'Player {p} vs Computer {s}. {pl_lose}')

        elif player_move() == 'p' and computer_move() == 'r':
            pl_win_cnt += 1
            print(f'Player {p} vs Computer {r}. {pl_win}')

    return pl_win_cnt, com_win_cnt

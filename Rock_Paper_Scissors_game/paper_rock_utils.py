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

    while pl_win_cnt != 3 and com_win_cnt != 3:
        p_result = player_move()
        com_result = computer_move()

        if p_result == com_result:
            print(f'EQUALITY: {p_result} vs {com_result}')

        elif p_result == 'r' and com_result == 'p':
            com_win_cnt += 1
            print(f'Player {r} vs Computer {p}. {pl_lose}')

        elif p_result == 's' and com_result == 'r':
            com_win_cnt += 1
            print(f'Player {s} vs Computer {r}. {pl_lose}')

        elif p_result == 's' and com_result == 'p':
            pl_win_cnt += 1
            print(f'Player {s} vs Computer {p}. {pl_win}')

        elif p_result == 'p' and com_result == 's':
            pl_win_cnt += 1
            print(f'Player {p} vs Computer {s}. {pl_lose}')

        elif p_result == 'p' and com_result == 'r':
            pl_win_cnt += 1
            print(f'Player {p} vs Computer {r}. {pl_win}')

        elif p_result == 'r' and com_result == 's':
            pl_win_cnt += 1
            print(f'Player {p} vs Computer {r}. {pl_win}')

    return pl_win_cnt, com_win_cnt

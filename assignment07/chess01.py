import time

my_time = 0.1
opp_time = 0.5
opp = 3
pair_moves = 30


def game_each_board(x):
    board_start_time = time.perf_counter()
    for i in range(pair_moves):
        time.sleep(my_time)
        print(f'BOARD {x+1} {i+1} my_time move')
        time.sleep(opp_time)
        print(f'BOARD {x+1} {i+1} opponent_time move')
    print(f'BOARD {x+1} >>>>>>> Finished move in {round(time.perf_counter()-board_start_time)} sec\n')
    return round(time.perf_counter()-board_start_time)

if __name__ == '__main__':
    start_time = time.perf_counter()
    # Loops 24 times because we are playing 24 opponents.
    board_time = 0
    for board in range(opp):
        board_time += game_each_board(board)
    print(f'Board exhibition in {board_time} secs.')
    print(f'Finished in {round(time.perf_counter()-start_time)} secs.')
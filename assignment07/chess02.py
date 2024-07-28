import asyncio
import time

my_time = 0.1
opp_time = 0.5
opp = 24
pair_moves = 30


async def game_each_board(x):
    board_start_time = time.perf_counter()
    for i in range(pair_moves):
        # Don't use time.sleep in a async function.I'm using it because in reality u aren't thinking about making a move on multi-board
        # Move on 24 boards at the same time, and so I need to block the evnt loop
        time.sleep(my_time)
        print(f'BOARD {x+1} {i+1} my_time move')
        await asyncio.sleep(opp_time)
        print(f'BOARD {x+1} {i+1} opponent_time move')
    print(f'BOARD {x+1} >>>>>>> Finished move in {round(time.perf_counter()-board_start_time)} sec\n')
    return round(time.perf_counter()-board_start_time)

async def async_io():
    tasks = []
    for i in range(opp):
        tasks += [game_each_board(i)]
    await asyncio.gather(*tasks)
    print(f'Board exhibition in {round(time.perf_counter()-start_time)} secs.')


if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f'Finished in {round(time.perf_counter()-start_time)} secs.')
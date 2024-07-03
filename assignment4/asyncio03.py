# example of gather for many coroutines in a list
# example of starting many tasks and getting access to all tasks
import asyncio

# coroutine for a task
async def task_coro(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)

# coroutine used for the entry point
async def main():
    # report a meassage
    print('main starting')
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # run the tasks
    await asyncio.gather(*coros)
    print('main done')

# started the asyncio program
asyncio.run(main())
from random import random
import asyncio

# coroutine to execute in a new task
async def task_rice():
    # generate a random value between 0 to 1
    val_rice = random() + 1
    # block for a moment
    print(f'>Task (Rice) done with {val_rice:.2f} sec')
    await asyncio.sleep(val_rice)
    return val_rice

          
async def task_noodle():
    # generate a random value between 0 to 1
    val_noodle = random() + 1
    # block for a moment
    print(f'>Task (Noodle) done with {val_noodle:.2f} sec')
    await asyncio.sleep(val_noodle)
    return val_noodle


async def task_curry():
    # generate a random value between 0 to 1
    val_cur = random() + 1
    # block for a moment
    print(f'>Task (Curry) done with {val_cur:.2f} sec' )
    await asyncio.sleep(val_cur)
    return val_cur

# main coroutine
async def main():
    #create many tasks
    r_task = asyncio.create_task(task_rice(),name="Rice")
    n_task = asyncio.create_task(task_noodle(),name="Noodle")
    c_task = asyncio.create_task(task_curry(),name="Curry")
    # wait for all tasks to complete
    done, pending = await asyncio.wait([r_task, n_task, c_task], return_when=asyncio.FIRST_COMPLETED)
    # report results
    for task in done:
        print(f'>Task ({task.get_name()}) is the first completed task with {task.result():.2f} sec')

# start the asyncio program
asyncio.run(main())
import asyncio, time


def wait():
    time.sleep(2)

    with open("test.txt", "w") as f:
        f.write("Finished in 2 seconds")


async def main():
    print("Hello")
    wait()
    print("goodbye")
    return "Yes!"

# loop = asyncio.get_event_loop()
# task = main()
# print(loop, task)
# all_tasks = asyncio.all_tasks(loop=loop)  # Typically to get the result: loop through all the tasks calling the `result()` method on each individual task
# loop.run_until_complete(task)
# print(all_tasks)

coro = main()

asyncio.get_event_loop()

# coro.throw(Exception)

import ipdb; ipdb.set_trace()

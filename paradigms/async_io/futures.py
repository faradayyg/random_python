import asyncio

"""Two things re generated here:
    1: The internals of what the event loop does with the coroutines
        A StopIteration exception is raised when your coroutine finishes:
        This is by design and you typically do not have to interact with this
        Whatever the return is from your coroutine will be returned as the object of the exception
    2: Futures, and how they work(?)
    3: The third part with fut2 demonstrates how to actually execute a task with the native
        event loop available and the StopIteration properly handled
"""


async def main(f: asyncio.Future):
    try:
        lp = asyncio.get_running_loop()
        print(lp, asyncio.all_tasks(loop=lp))
        f.set_result("Found loop")
    except RuntimeError as e:
        print("Could not find running loop", e)
        f.set_result("Injected result, failed loop")
    return True


fut = asyncio.Future()

print(fut)


# This is what happens within the event loop when called
coro = main(fut)

try:
    coro.send(None)
except StopIteration as e:
    print(e)

print(fut)

print(">>"*10)


# This is how to properly execute an async task
fut2 = asyncio.Future()


print("fut2", fut2)
asyncio.run(main(fut2))
print("fut2", fut2)

"""Demonstrates as async iterator."""
from typing import Iterable
import asyncio


class AsyncIter():
    def __init__(self, keys: Iterable) -> None:
        self.keys = keys

    def __aiter__(self) -> Iterable:
        """An iter should return an iterable object on which .next() can be called
        In our case, we return self because next can be called on it
        """
        self.ikeys = iter(self.keys)
        return self

    async def __anext__(self):
        try:
            await sleep_next() # coro things can be done in here because it's async
            return next(self.ikeys)
        except StopIteration:
            raise StopAsyncIteration


async def sleep_next():
    await asyncio.sleep(1)


async def main():
    iter = AsyncIter([1,2,3])
    async for i in iter:
        print(i)

asyncio.run(main())

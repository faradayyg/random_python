import asyncio
from typing import Iterable

async def generator(keys):
    for k in keys:
        await asyncio.sleep(0.4)
        yield k


async def main():
    async for i in generator(["one", "more", "time"]):
        print(i)

asyncio.run(main())

import asyncio
import aiohttp
import contextlib
import time


@contextlib.asynccontextmanager
def timed():
    start = time.time()
    yield
    end = time.time()
    print(">>>>", end-start, " <<<<<<")


async def main():
    for i in range(2):
        await get_web_page()


async def get_web_page():
    asyncio.sleep(1)
    # url = 'http://santa.fridaygodswill.com/'
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(url) as response:
    #         html = await response.text()
    #         return html


start = time.time()
h = asyncio.run(main())
end = time.time()
print(">>>>", end-start, " <<<<")
# import ipdb; ipdb.set_trace()

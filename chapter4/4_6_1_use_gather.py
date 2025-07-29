import asyncio
import aiohttp
from aiohttp import ClientSession
#from util import async_timed, fetch_status
import time


async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


# @async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        # import random
        # delay = random.randint(1, 5)
        #url = f'http://127.0.0.1:8000/get_info?n={delay}'
        urls = [url for _ in range(1000)]
        # urls = [f'http://127.0.0.1:8000/get_info?n={random.randint(1, 5)}' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        await asyncio.gather(*requests)
        # print(status_codes)

start = time.perf_counter()
asyncio.run(main())
print(time.perf_counter() - start)

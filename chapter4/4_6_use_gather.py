import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed
import time


async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://example.com'
        # url = 'https://profi-mag.com/'
        urls = [url for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)

# start = time.perf_counter()
asyncio.run(main())
# print(time.perf_counter() - start)

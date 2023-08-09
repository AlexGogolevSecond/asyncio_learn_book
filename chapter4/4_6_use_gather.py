import asyncio
import aiohttp
from util import async_timed, fetch_status
import time


# @async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        await asyncio.gather(*requests)
        # print(status_codes)

start = time.perf_counter()
asyncio.run(main())
print(time.perf_counter() - start)

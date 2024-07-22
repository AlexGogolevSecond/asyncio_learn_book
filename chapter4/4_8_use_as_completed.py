import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://www.example.com', 10),
                    fetch_status(session, 'https://www.example.com', 3),
                    fetch_status(session, 'https://www.example.com', 4)]
        for finished_task in asyncio.as_completed(fetchers):
            print(type(finished_task))
            res = await finished_task
            print(f'res: {res}')  # т.е.тут получаем результаты по мере получения результатов, а не в порядке как были вызовы

asyncio.run(main())

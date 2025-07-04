import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Абсолютный импорт
from util.async_timer import async_timed
from util.fetch_status import fetch_status


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

# Вывод:
# выполняется func=<function main at 0x7d798f3b0180> с аргументами args=(); kwargs={}
# <class 'coroutine'>
# выполняется func=<function fetch_status at 0x7d798f3b0400> с аргументами args=(<aiohttp.client.ClientSession object at 0x7d798f38a4b0>, 'https://www.example.com', 4); kwargs={}
# выполняется func=<function fetch_status at 0x7d798f3b0400> с аргументами args=(<aiohttp.client.ClientSession object at 0x7d798f38a4b0>, 'https://www.example.com', 10); kwargs={}
# выполняется func=<function fetch_status at 0x7d798f3b0400> с аргументами args=(<aiohttp.client.ClientSession object at 0x7d798f38a4b0>, 'https://www.example.com', 3); kwargs={}
# <function fetch_status at 0x7d798f3b0400> завершилась за 3.1604 с
# res: result.status=200; delay=3
# <class 'coroutine'>
# <function fetch_status at 0x7d798f3b0400> завершилась за 4.0143 с
# res: result.status=200; delay=4
# <class 'coroutine'>
# <function fetch_status at 0x7d798f3b0400> завершилась за 10.0172 с
# res: result.status=200; delay=10
# <function main at 0x7d798f3b0180> завершилась за 10.0205 с
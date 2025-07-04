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
                    fetch_status(session, 'https://www.example.com', 3),
                    fetch_status(session, 'https://www.example.com', 5)]
        # asyncio.as_completed(fetchers)  # так просто нельзя:
        #         выполняется func=<function main at 0x7e55201ec180> с аргументами args=(); kwargs={}
        # /home/alex/py_tmp/asyncio_learn_book/util/async_timer.py:13: RuntimeWarning: coroutine 'fetch_status' was never awaited
        #   return await func(*args, **kwargs)
        # RuntimeWarning: Enable tracemalloc to get the object allocation traceback
        # <function main at 0x7e55201ec180> завершилась за 0.0051 с

        for finished_task in asyncio.as_completed(fetchers, timeout=4):
            try:
                res = await finished_task
                print(f'res: {res}')  # т.е.тут получаем результаты по мере получения результатов, а не в порядке как были вызовы
            except asyncio.TimeoutError:
                print(f'Задача {finished_task} превысила таймаут и была отменена')

asyncio.run(main())

# Вывод:
# выполняется func=<function main at 0x753d60174220> с аргументами args=(); kwargs={}
# выполняется func=<function fetch_status at 0x753d601744a0> с аргументами args=(<aiohttp.client.ClientSession object at 0x753d6015a060>, 'https://www.example.com', 3); kwargs={}
# выполняется func=<function fetch_status at 0x753d601744a0> с аргументами args=(<aiohttp.client.ClientSession object at 0x753d6015a060>, 'https://www.example.com', 3); kwargs={}
# выполняется func=<function fetch_status at 0x753d601744a0> с аргументами args=(<aiohttp.client.ClientSession object at 0x753d6015a060>, 'https://www.example.com', 5); kwargs={}
# выполняется func=<function fetch_status at 0x753d601744a0> с аргументами args=(<aiohttp.client.ClientSession object at 0x753d6015a060>, 'https://www.example.com', 10); kwargs={}
# <function fetch_status at 0x753d601744a0> завершилась за 3.1053 с
# res: result.status=200; delay=3
# <function fetch_status at 0x753d601744a0> завершилась за 3.1088 с
# res: result.status=200; delay=3
# Задача <coroutine object as_completed.<locals>._wait_for_one at 0x753d60f845f0> превысила таймаут и была отменена
# Задача <coroutine object as_completed.<locals>._wait_for_one at 0x753d6041f850> превысила таймаут и была отменена
# <function main at 0x753d60174220> завершилась за 4.0063 с
# <function fetch_status at 0x753d601744a0> завершилась за 4.0060 с
# <function fetch_status at 0x753d601744a0> завершилась за 4.0061 с
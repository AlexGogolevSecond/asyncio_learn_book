import asyncio
import logging
import aiohttp
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
        first_request = fetch_status(session, 'https://www.example.com', 5)
        # bad_request = fetch_status(session, 'python://bad')
        second_request = fetch_status(session, 'https222://www.example.com', 1)
        third_request = fetch_status(session, 'https://www.example.com', 2)
        fetchers = [asyncio.create_task(first_request),
                    asyncio.create_task(second_request),
                    asyncio.create_task(third_request)]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.ALL_COMPLETED)
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')
        for done_task in done:
            # result = await done_task возбудит исключение
            if done_task.exception() is None:
                print('done_task.result(): ' + str(done_task.result()))
            else:
                logging.error("При выполнении запроса возникло исключение",
                              exc_info=done_task.exception())

asyncio.run(main())

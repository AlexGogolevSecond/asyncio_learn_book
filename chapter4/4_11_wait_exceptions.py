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
        good_request = fetch_status(session, 'https://www.example.com')
        bad_request = fetch_status(session, 'python://bad')
        # bad_request = fetch_status(session, 'https://www.example.com')
        fetchers = [asyncio.create_task(good_request),
                    asyncio.create_task(bad_request)]
        done, pending = await asyncio.wait(fetchers)
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')
        for done_task in done:
            # result = await done_task возбудит исключение
            if done_task.exception() is None:
                print(f'{done_task.result()=}')
            else:
                logging.error("При выполнении запроса возникло исключение",
                              exc_info=done_task.exception())

asyncio.run(main())

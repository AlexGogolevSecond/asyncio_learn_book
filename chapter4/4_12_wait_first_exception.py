import aiohttp
import asyncio
import logging
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
        fetchers = [asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=3)),
                    asyncio.create_task(fetch_status(session, 'python://bad.com')),
                    asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=3))]

        done, pending = await asyncio.wait(fetchers,
                                           return_when=asyncio.FIRST_EXCEPTION)
        print(f'Число завершившихся задач: {len(done)}')  # == 1 - это з-ча, которая завершилась с исключением
        print(f'Число ожидающих задач: {len(pending)}')  # == 2 - это те 2 з-чи с таймаутом 3
        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("При выполнении запроса возникло исключение", 
                            exc_info=done_task.exception())
        for pending_task in pending:
            pending_task.cancel()  # и походу тут мы отменяем нафиг те 2 з-чи с таймаутом


asyncio.run(main())      

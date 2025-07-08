import asyncio
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
        url = 'https://www.example.com'
        fetchers = [asyncio.create_task(fetch_status(session, url, 4)),
                    asyncio.create_task(fetch_status(session, url,2)),
                    asyncio.create_task(fetch_status(session, url, 3))]

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)
        # print(f'Число завершившихся задач: {len(done)}')
        # print(f'Число ожидающих задач: {len(pending)}')
        print(f"Завершено: {len(done)}, Ожидают: {len(pending)}")
        for done_task in done:
            print(await done_task)  # тут будет только одна задача, т.к. return_when=FIRST_COMPLETED

        for pending_task in pending:
            print(f'{pending_task=}')

asyncio.run(main())

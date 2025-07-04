"""Если возникают исключения, то программа не падает и не нужно обрабатывать их через try/except"""

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
        urls = ['https://example.com', 'python://example.com', 'https://google.com']
        tasks = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        exceptions = [res for res in results if isinstance(res, Exception)]
        successful_results = [res for res in results if not isinstance(res, Exception)]
        print('*' * 25)
        print(f'Все результаты: {results=}')
        print(f'Завершились успешно: {successful_results=}')
        print(f'Завершились с исключением: {exceptions=}')

asyncio.run(main())

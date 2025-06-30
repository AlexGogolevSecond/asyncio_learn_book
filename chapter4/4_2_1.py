import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Абсолютный импорт
from util.async_timer import async_timed
from util.fetch_status import fetch_status
import asyncio
import aiohttp
from aiohttp import ClientSession


# @async_timed()
# async def fetch_status(session: ClientSession, url: str) -> int:
#     async with session.get(url) as result:
#         return result.status
    
@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f'Состояние для {url} было равно {status}')

asyncio.run(main())



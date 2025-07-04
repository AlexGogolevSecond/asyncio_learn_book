"""Отправка веб-запроса с по­мощью aiohttp"""
import asyncio
import aiohttp
from aiohttp import ClientSession
# from util import async_timed
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Абсолютный импорт
from util.async_timer import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    conn = aiohttp.TCPConnector(limit=200)  # Ограничение на количество соединений (по умолчанию 100)
    async with aiohttp.ClientSession(connector=conn) as session:
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f'status для {url}: {status}')


asyncio.run(main())

"""Задание тайм-аутов в aiohttp"""
import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=2.51)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status


async def main():
    session_timeout = aiohttp.ClientTimeout(total=5, connect=1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        status = await fetch_status(session, 'https://mail.com')
        print(f'{status=}')


asyncio.run(main())

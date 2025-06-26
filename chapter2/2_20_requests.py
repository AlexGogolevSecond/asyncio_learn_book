import asyncio
import requests
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Абсолютный импорт
from util.async_timer import async_timed

@async_timed()
async def get_status_code() -> int:
    return requests.get('http://example.com').status_code

@async_timed()
async def main():
    t1 = asyncio.create_task(get_status_code())
    t2 = asyncio.create_task(get_status_code())
    t3 = asyncio.create_task(get_status_code())
    await t1
    await t2
    await t3

asyncio.run(main())
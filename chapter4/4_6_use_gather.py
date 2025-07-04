import asyncio
import aiohttp
from aiohttp import ClientSession
# from util import async_timed
import time
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Абсолютный импорт
from util.async_timer import async_timed
from util.fetch_status import fetch_status

# async def fetch_status(session: ClientSession, url: str) -> int:
#     async with session.get(url) as result:
#         return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        # 1 значение с временем - впн через мск, 2-й - Пермь
        url = 'https://example.com'  # 3.8980 с    2.9833 с
        # url = 'https://profi-mag.com/'  # 13.6216 с    exception after 140.2249 с
        # url = 'https://sbis.ru/'  # 9.5578 с    exception after 65.8625 с
        # url = 'https://ya.ru/'  # 8.3910 с    6.6704 с
        # url = 'https://mail.ru/'  # 7.6631 с    6.5571 с
        # url = 'https://google.com/'  # 8.1559 с    6.4422 с
        # url = 'https://google.ru/'  # 7.2605 с    exception after 136.2286 с
        # url = 'https://bigbird.ru/'  # 64.3746 с     88.1235 с

        urls = [url for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        # print(status_codes)

start = time.perf_counter()
asyncio.run(main())
print(time.perf_counter() - start)  # 2.2851 с. - example.com НЕ через отладку а напрямую в консоли и без принтов по статусам

import time
import threading
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import asyncio
import requests
import aiohttp
from time import perf_counter


def sync_download(url):
    response = requests.get(url)
    return response.status_code

async def async_download(session, url):
    async with session.get(url) as response:
        return response.status

def test_sync():
    start = time.time()
    for _ in range(10):
        sync_download("https://httpbin.org/get")
    return time.time() - start

def test_threads():
    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        list(executor.map(sync_download, ["https://httpbin.org/get"] * 10))
    return time.time() - start

async def test_async():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [async_download(session, "https://httpbin.org/get") for _ in range(10)]
        await asyncio.gather(*tasks)
    return time.time() - start

# Запуск тестов
print(f"Синхронно: {test_sync():.2f}с")
print(f"Потоки: {test_threads():.2f}с")
st = perf_counter()
asyncio.run(test_async())  # Будет быстрее для I/O
fin = perf_counter()
print(f'Time asyncio: {fin - st:.2f} seconds')

# Вывод:
"""
Синхронно: 28.12с
Потоки: 3.73с
Time asyncio: 2.20 seconds
"""
import functools
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time
# from util import async_timed


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


# @async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=1000) as pool:  # без указания max_workers выполняется примерно за 25 секунд, с max_workers=1000 за 2,5 секунды
        urls = ['https://www.example.com' for _ in range(1000)]
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        # print(results)

st = time.time()
asyncio.run(main())
print(f'{time.time() - st}')

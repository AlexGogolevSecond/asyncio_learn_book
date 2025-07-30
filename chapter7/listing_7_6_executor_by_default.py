import functools
import requests
import asyncio
from time import perf_counter


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


async def main():
    loop = asyncio.get_running_loop()
    urls = ['https://www.example.com' for _ in range(1000)]
    tasks = [loop.run_in_executor(None, functools.partial(get_status_code, url)) for url in urls]
    results = await asyncio.gather(*tasks)
    # print(results)

st = perf_counter()
asyncio.run(main())
fin = perf_counter()
print(f'Time taken: {fin - st:.2f} seconds')

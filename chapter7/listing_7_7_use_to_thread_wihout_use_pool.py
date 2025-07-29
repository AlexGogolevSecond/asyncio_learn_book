import requests
import asyncio
import time
# from util import async_timed


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


# @async_timed()
async def main():
    urls = ['https://www.example.com' for _ in range(1000)]
    tasks = [asyncio.to_thread(get_status_code, url) for url in urls]
    results = await asyncio.gather(*tasks)
    # print(results)

st = time.time()
asyncio.run(main())
print(f'{time.time() - st}')

'''
даже на цикле в 100 элементов выполняется 6.477180 с
'''
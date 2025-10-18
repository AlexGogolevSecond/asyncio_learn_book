import functools
from concurrent.futures.thread import ThreadPoolExecutor
import numpy as np
import asyncio
# from util import async_timed


def mean_for_row(arr, row):
    return np.mean(arr[row])


data_points = 500_000_000 # 4_000_000_000
rows = 50
columns = int(data_points / rows)

matrix = np.arange(data_points).reshape(rows, columns)

# @async_timed()
async def main():
    import time
    s = time.time()
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        tasks = []
        for i in range(rows):
            mean = functools.partial(mean_for_row, matrix, i)
            tasks.append(loop.run_in_executor(pool, mean))

        results = asyncio.gather(*tasks)
    f = time.time()
    print(f'{f - s}')

asyncio.run(main())

import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List
from time import perf_counter


def count(count_to: int) -> int:
    '''т.е. метод м.б. даже не синхронным'''    
    start = perf_counter()
    counter = 0
    while counter < count_to:
        counter += 1
    end = perf_counter()
    print(f'Закончен подсчет до {count_to} за время {end-start}')
    return counter


async def main():
    with ProcessPoolExecutor() as process_pool:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        nums = [1_000_000, 22_000_000, 100_000_000, 5_000_000, 3_000_000]
        calls: List[partial[int]] = [partial(count, num) for num in nums]
        call_coros = []
        for call in calls:
            call_coros.append(loop.run_in_executor(process_pool, call))  #  тут можно использовать только "частичное применение функции" - стр 164

        results = await asyncio.gather(*call_coros)
        print('перед циклом results')
        for result in results:
            print(result)


if __name__ == "__main__":
    asyncio.run(main())

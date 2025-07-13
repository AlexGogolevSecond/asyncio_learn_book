import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
import functools
from typing import List
from time import perf_counter


def count(count_to: int) -> int:
    '''т.е. метод м.б. даже не асинхронным'''
    start = perf_counter()
    counter = 0
    while counter < count_to:
        counter += 1
    end = perf_counter()
    print(f'Закончен подсчет до {count_to} за время {end-start}')
    return counter


async def main():
    with ProcessPoolExecutor() as process_pool_executor:
        st = perf_counter()

        loop: AbstractEventLoop = asyncio.get_running_loop()
        # nums = [1_000_000, 22_000_000, 100_000_000, 5_000_000, 3_000_000]
        nums = [100_000_000, 1, 3, 5, 22, 200_000_000]
        calls: List[functools.partial[int]] = [functools.partial(count, num) for num in nums]
        call_coros = []
        # for call in calls:
        #     call_coros.append(loop.run_in_executor(process_pool, call))  # тут можно использовать только "частичное применение функции" - стр 164
        #                                                                  # т.е. при част. прим-ии функции нельзя передавать аргументы при вызове метода,
        #                                                                  # для этого исп-ся functools.partial
        for num in nums:
            call_coros.append(loop.run_in_executor(process_pool_executor, count, num))  # вообще-то так тоже работает - передача параметра, причём даже быстрее чем частичное применение
        results = await asyncio.gather(*call_coros)  # ждём получения результатов
        print('перед циклом results')
        for result in results:
            print(result)

        print(f'итого: {perf_counter() - st}')  # при использовании asyncio всегда получается быстрее чем просто пулом процессов:
                                                #  пулами - (7.04 - 7.37) c.; с asyncio - (6.73 - 6.76) c.

if __name__ == "__main__":
    asyncio.run(main())


'''
Закончен подсчет до 1 за время 2.9330039978958666e-06
Закончен подсчет до 5 за время 3.3519972930662334e-06
Закончен подсчет до 3 за время 4.1900057112798095e-06
Закончен подсчет до 22 за время 6.704998668283224e-06
Закончен подсчет до 100000000 за время 3.6143106749950675
Закончен подсчет до 200000000 за время 6.7465162350054015
перед циклом results
100000000
1
3
5
22
200000000
итого: 6.761519512998348
'''
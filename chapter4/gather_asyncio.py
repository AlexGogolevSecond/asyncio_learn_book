import asyncio
from time import perf_counter


async def sl(n: int) -> None:
    # if n == 1:
    #     raise Exception
    await asyncio.sleep(n)


async def main():
    start = perf_counter()

    task1 = sl(5)
    task2 = sl(3)
    task3 = sl(1)
    task4 = sl(4)
    task5 = sl(3)

    await asyncio.gather(task1, task2, task3, task4, task5)

    print(perf_counter() - start)


asyncio.run(main())

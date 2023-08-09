import asyncio
from time import perf_counter


async def sl(n: int) -> None:
    await asyncio.sleep(n)


async def main():
    start = perf_counter()

    task1 = sl(5)
    task2 = sl(3)

    await asyncio.gather(task1, task2)

    print(perf_counter() - start)


asyncio.run(main())

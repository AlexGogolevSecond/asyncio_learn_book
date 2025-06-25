import asyncio
import time


async def sl(n):
    print(f'засыпаю на {n} с.')
    await asyncio.sleep(n)
    print(f'проснулся после сна {n} с.')


async def main():
    start = time.time()
    t1 = asyncio.create_task(sl(3))
    t2 = asyncio.create_task(sl(4))
    # await t1
    # await t2  # время выполнения 4 с, т.е. конкурентно
    # await asyncio.create_task(sl(3))
    # await asyncio.create_task(sl(4))
    
    # await asyncio.gather(t1, t2)  # можно и корутины передавать и задачи
    await asyncio.gather(sl(3), sl(4))

    finish = time.time()
    print(finish - start)

asyncio.run(main())

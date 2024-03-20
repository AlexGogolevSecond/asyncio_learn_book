import asyncio
import time


async def sl(n):
    await asyncio.sleep(n)


async def main():
    start = time.time()
    t1 = asyncio.create_task(sl(3))
    t2 = asyncio.create_task(sl(4))
    # await t1
    # await t2
    # await asyncio.create_task(sl(3))
    # await asyncio.create_task(sl(4))
    
    await asyncio.gather(t1, t2)  # можно и корутины передавать и задачи

    finish = time.time()
    print(finish - start)

asyncio.run(main())

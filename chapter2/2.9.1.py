import asyncio
import time


async def sl(n) -> None:
    print(f'засыпаю на {n} с.')
    await asyncio.sleep(n)
    print(f'проснулся после сна {n} с.')


async def main():
    start = time.time()
    t1 = asyncio.create_task(sl(3))
    t2 = asyncio.create_task(sl(4))
    await t1
    await t2
    # await asyncio.create_task(sl(3))
    # await asyncio.create_task(sl(4))
    
    # await asyncio.gather(t1, t2)  # можно и корутины передавать и задачи
    
    # await asyncio.gather(sl(3), sl(4))

    # await sl(3)  # смысла вызывать через await сопрограмму нет, т.к. сопрограмма будет выполняться пока не выполнится, т.е.
    # await sl(4)  # обычное синхронное выполнение. Т.е. на каждой такой строке родительская сопрограмма приостанавливается
                   #  и ждёт результата

    finish = time.time()
    print(finish - start)

asyncio.run(main())

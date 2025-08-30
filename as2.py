import asyncio
import random
# import time
from datetime import datetime


async def some(i):
    n = random.randint(1, 10)
    await asyncio.sleep(n)
    print(f'{datetime.today().strftime("%H:%M:%S")} {i} спал {n} c')
    
    return (i, n)


async def main():
    print(f'начало: {datetime.today().strftime("%H:%M:%S")}')
    tasks = []
    for i in range(10):
        task = asyncio.create_task(some(i))
        tasks.append(task)
    print(f'окончание цикла с create_task: {datetime.today().strftime("%H:%M:%S")}')
    print('-'*25)
    result = {}
    c = 0
    for task in tasks:
        res = await task
        print(f'обработана таска {res}')
        result.update({c: (res, datetime.today().strftime("%H:%M:%S"))})
        c += 1

    # b = 0
    print('*'*25)
    print(f'{datetime.today().strftime("%H:%M:%S")} result: {result}')


asyncio.run(main())

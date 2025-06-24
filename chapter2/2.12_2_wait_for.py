"""Снятие задачи по таймауту"""

import asyncio
from util import delay


async def main():
    delay_task = asyncio.create_task(delay(2))

    try:
        result = await asyncio.wait_for(delay(2), timeout=1)
        print(f'{result=}')
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        # print(f'Задача была снята? - {delay(2).cancelled()}')

asyncio.run(main())

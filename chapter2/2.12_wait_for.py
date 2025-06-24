"""Снятие задачи по таймауту"""

import asyncio
from util import delay


async def main():
    delay_task = asyncio.create_task(delay(2))

    try:
        result = await asyncio.wait_for(delay_task, timeout=1)  # !!! СУПЕР ВАЖНО - если метод, который передаётся wait_for не вызывает ничего
        # асинхронного, (например м.б. бесконечный цикл с синхронным кодом, то в event loop управление никогда не вернётся, и wait_for будет ждать
        # бесконечно, т.е. timeout не сработает)
        print(f'{result=}')
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? - {delay_task.cancelled()}')

asyncio.run(main())

import asyncio
from asyncio import CancelledError

from util import delay

# async def delay(delay_seconds: int) -> int:
#     print(f'засыпаю на {delay_seconds} с')
#     await asyncio.sleep(delay_seconds)
#     print(f'сон в течение {delay_seconds} с закончился')
#     return delay_seconds


async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0

    while not long_task.done():
        print(f'{seconds_elapsed=} Задача не закончилась, следующая проверка через секунду.')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print('Наша задача была снята')

asyncio.run(main())

import asyncio
#from util import delay, async_timed
import time
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Абсолютный импорт
from util.async_timer import async_timed
from util.fetch_status import fetch_status
from util.delay_functions import delay


async def positive_integers_async(until: int):
    for integer in range(1, until):
        # await delay(3)
        await delay(until)
        yield integer


@async_timed()
async def main():
    async_generator111 = positive_integers_async(3)  # type async_generator
    print(type(async_generator111))
    async for number in async_generator111:
        print(f'Получено число {number}')


start = time.perf_counter()
asyncio.run(main())
print(f'{time.perf_counter() - start}')

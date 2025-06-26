import asyncio
# from ..util import async_timed
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Абсолютный импорт
from util.async_timer import async_timed
from util.delay_functions import delay

@async_timed()
async def cpu_bound_work(n: int) -> int:
    counter = 0
    for i in range(n):
        counter += 1
    return counter

@async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bound_work(100000000))
    task_two = asyncio.create_task(cpu_bound_work(100000000))
    delay_task = asyncio.create_task(delay(3))
    await task_one
    await task_two
    await delay_task

asyncio.run(main())

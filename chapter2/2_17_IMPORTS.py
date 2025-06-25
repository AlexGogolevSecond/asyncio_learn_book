import asyncio
# from ..util import async_timed
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Абсолютный импорт
from util.async_timer import async_timed



@async_timed()
async def delay(delay_seconds: int) -> int:
/*************  ✨ Windsurf Command ⭐  *************/
    """Async function that waits for a given number of seconds, then returns."""

/*******  9ac1bd51-077e-4d95-9dd4-a180ccf28125  *******/
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds

@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))
    await task_one
    await task_two

asyncio.run(main())

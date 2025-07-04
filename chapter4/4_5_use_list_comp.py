import asyncio
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Абсолютный импорт
from util.async_timer import async_timed
from util.delay_functions import delay


@async_timed()
async def main() -> None:
    delay_times = [3, 3, 3]
    tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_times]
    [await task for task in tasks]

asyncio.run(main())

# Вывод:
# выполняется func=<function main at 0x00000253477B1440> с аргументами args=(); kwargs={}
# засыпаю на 3 с
# засыпаю на 3 с
# засыпаю на 3 с
# сон в течение 3 с закончился
# сон в течение 3 с закончился
# сон в течение 3 с закончился
# <function main at 0x00000253477B1440> завершилась за 3.0079 с

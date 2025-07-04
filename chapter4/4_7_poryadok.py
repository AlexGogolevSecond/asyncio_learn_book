"""Завершение допускающих ожидание объектов не по порядку"""

import asyncio
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Абсолютный импорт
from util.async_timer import async_timed
from util.fetch_status import fetch_status
from util.delay_functions import delay


async def main():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)


asyncio.run(main())

# засыпаю на 3 с
# засыпаю на 1 с
# сон в течение 1 с закончился
# сон в течение 3 с закончился
# [3, 1]

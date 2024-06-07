"""Завершение допускающих ожидание объектов не по порядку"""

import asyncio
from util import delay


async def main():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)


asyncio.run(main())

# засыпаю на 3 с
# засыпаю на 1 с
# сон в течение 1 с закончился
# сон в течение 3 с закончился
# [3, 1]

import asyncio
#from util import delay, async_timed
import time


async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def positive_integers_async(until: int):
    for integer in range(1, until):
        # await delay(3)
        await delay(integer)
        yield integer


#@async_timed()
async def main():
    async_generator111 = positive_integers_async(3)  # type async_generator
    print(type(async_generator111))
    async for number in async_generator111:
        print(f'Получено число {number}')


start = time.perf_counter()
asyncio.run(main())
print(f'{time.perf_counter() - start}')

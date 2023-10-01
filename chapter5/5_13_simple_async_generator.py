import asyncio
#from util import delay, async_timed


async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def positive_integers_async(until: int):
    for integer in range(1, until):
        await delay(integer)
        yield integer


#@async_timed()
async def main():
    async_generator = positive_integers_async(3)
    print(type(async_generator))
    async for number in async_generator:
        print(f'Получено число {number}')


asyncio.run(main())
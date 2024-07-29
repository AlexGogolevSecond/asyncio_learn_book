import asyncio
# from ..delay_functions import 


async def main():
    while True:
        delay_time = input('Enter a time to sleep:')
        asyncio.create_task(asyncio.sleep(int(delay_time)))


asyncio.run(main())

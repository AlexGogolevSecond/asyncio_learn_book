"""создание цикла событий вручную"""
import asyncio


async def main():
    print(f'засыпаю на 1 с.')
    await asyncio.sleep(1)
    print(f'просыпаюсь после сна 1 с.')

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

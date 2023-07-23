import asyncio
from util import delay


async def main():
    delay_task = asyncio.create_task(delay(5))
    try:
        result = await asyncio.wait_for(delay_task, timeout=3)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? {delay_task.cancelled()}')
        result = None
    
    if not result:
        print('Вышли по таймауту!')

asyncio.run(main())

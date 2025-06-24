import asyncio
from util import delay
from datetime import datetime


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("пока я жду, исполняется другой код!")


async def main():
    print(f"Создаём first_delay в {datetime.now().time()}")
    first_delay = asyncio.create_task(delay(3))
    print(f"Создаём second_delay в {datetime.now().time()}")
    second_delay = asyncio.create_task(delay(3))
    
    await hello_every_second()
    
    print(f"Ждём first_delay в {datetime.now().time()}")
    await first_delay
    print(f"Ждём second_delay в {datetime.now().time()}")
    await second_delay

asyncio.run(main())

from util import delay
import asyncio
import time


async def lalala() -> None:
    st1 = time.perf_counter()
    await delay(3)
    await delay(4)
    fin1 = time.perf_counter()
    print(f'первые delay за {fin1 - st1} c')

    print('*' * 30)

    st2 = time.perf_counter()
    await asyncio.gather(delay(3), delay(4))
    fin2 = time.perf_counter()
    print(f'gather за {fin2 - st2} c')

asyncio.run(lalala())


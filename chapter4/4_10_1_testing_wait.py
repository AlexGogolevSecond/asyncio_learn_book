import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed
from util import fetch_status
import time

"""return_when может иметь след. значения: 
ALL_COMPLETED, FIRST_EXCEPTION и FIRST_COMPLETED"""

async def async_sl(n: int = None):
    if n:
        await asyncio.sleep(n)
        return f'спал {n} сек.'
    else:
        await asyncio.sleep(2)
        return 'спал 2 сек.'

# @async_timed()
async def main():
    st = time.time()
    fetchers = [asyncio.create_task(async_sl(3)),
                asyncio.create_task(async_sl(2))]

    done, pending = await asyncio.wait(fetchers, timeout=2.5)
    print(f'Число завершившихся задач: {len(done)}')
    print(f'Число ожидающих задач: {len(pending)}')  # в книге написано, что тут будет пусто, т.к. у нас тут по ум.
                                                        # режим return_when == ALL_COMPLETED. а в этом случае asyncio.wait
                                                        # не вернется, пока все не завершится
    fin = time.time()
    print(f'wait выполнился за: {fin - st} c')
    for done_task in done:
        # получаем результат
        result = await done_task  # из-за этого и падает если exception - см. 4.11/4.12
        print(result)
        # if done_task.exception is None:
        #     print(str(done_task.result()) + 'aaa')
        # else:
        #     print(str(done_task.exception()) + 'uuu')

    # except Exception as ex:
    #     print(str(ex))

asyncio.run(main())

'''
Вывод:
Число завершившихся задач: 1
Число ожидающих задач: 1
wait выполнился за: 2.5013320446014404 c
спал 2 сек.
'''

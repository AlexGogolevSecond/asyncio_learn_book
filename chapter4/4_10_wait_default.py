import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Абсолютный импорт
from util.async_timer import async_timed
from util.fetch_status import fetch_status


"""return_when может иметь след. значения:
ALL_COMPLETED, FIRST_EXCEPTION и FIRST_COMPLETED"""

# @async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://example.com')),
                    asyncio.create_task(fetch_status(session, 'https://example.com'))]
                    # asyncio.create_task(fetch_status(session, 'https22://example.com'))]
        # НО!!! если возникнет исключение (оно возникает при любом значении return_when),
        # то оно никуда не денется и программа упадёт, видимо его нужно обрабатывать

        # try:
        done, pending = await asyncio.wait(fetchers)  # done и pending - множества
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')  # в книге написано, что тут будет пусто, т.к. у нас тут по ум.
                                                         # режим return_when == ALL_COMPLETED. а в этом случае asyncio.wait
                                                         # не вернется, пока все не завершится
        for done_task in done:
            # получаем результат
            result = await done_task  # из-за этого и падает если exception - СМ. 4.11/4.12 !!!!
            print(result)
            # if done_task.exception is None:
            #     print(str(done_task.result()) + 'aaa')
            # else:
            #     print(str(done_task.exception()) + 'uuu')

        # except Exception as ex:
        #     print(str(ex))

asyncio.run(main())







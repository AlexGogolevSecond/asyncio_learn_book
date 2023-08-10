import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed
from util import fetch_status


# @async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://example.com')),
                    asyncio.create_task(fetch_status(session, 'https://example.com'))]
                    # asyncio.create_task(fetch_status(session, 'https22://example.com'))]
        # try:
        done, pending = await asyncio.wait(fetchers)
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')
        for done_task in done:
            result = await done_task
            print(result)
            # if done_task.exception is None:
            #     print(str(done_task.result()) + 'aaa')
            # else:
            #     print(str(done_task.exception()) + 'uuu')

        # except Exception as ex:
        #     print(str(ex))

asyncio.run(main())







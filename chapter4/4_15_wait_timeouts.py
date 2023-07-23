import aiohttp
import asyncio
import logging
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://example.com'
        fetchers = [asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url, delay=3))]
        done, pending = await asyncio.wait(fetchers, timeout=1)
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')
        for done_task in done:
            result = await done_task
            print(result)
        
        for pending_task in pending:
            pending_task.cancel()

asyncio.run(main())

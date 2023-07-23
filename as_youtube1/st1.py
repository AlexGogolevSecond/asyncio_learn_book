import asyncio


async def f():
    print('f() running')


async def g():
    await asyncio.sleep(5)
    print('g() completed')


async def main():
    # await g()
    # await f()
    task_g = main_loop.create_task(g())
    task_f = main_loop.create_task(f())

    await task_g
    await task_f


main_loop = asyncio.get_event_loop()
main_loop.run_until_complete(main())
# main_loop.run_forever()

from asyncio import Future
import asyncio

def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future

async def set_future_value(future) -> None:
    await asyncio.sleep(3)
    future.set_result(42)

async def main():
    future = make_request()
    print(f'1 Будущий объект готов? {future.done()}')
    value = await future
    print(f'2 Будущий объект готов? {future.done()}')
    print(value)

asyncio.run(main())

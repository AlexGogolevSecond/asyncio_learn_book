from util import delay
import asyncio


async def add_one(number: int) -> int:
    return number + 1

async def hello_world_message() -> str:
    await delay(3)
    return 'hello world!'  # это будет напечатано только через 3 с

async def main() -> None:
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(message)
    print(one_plus_one)
    # тут всё последовательно

asyncio.run(main())

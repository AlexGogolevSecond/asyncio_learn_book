import asyncio
import asyncpg
from connection import DATABASE_URL


async def main():
    connection = await asyncpg.connect(**DATABASE_URL)

    # query = 'SELECT product_id, product_name FROM product'
    query = 'select * from brand'
    async with connection.transaction():  # !!! обязательно д.б. транзакция
        async for data in connection.cursor(query, prefetch=10):  # выбираем по 50 (по умолчанию https://magicstack.github.io/asyncpg/current/api/index.html)
            print(f'{data=}')

    await connection.close()

# тут непонятно - получается, используя async for мы не загоняем в память все результаты запроса,
# а получаем их по 50
asyncio.run(main())
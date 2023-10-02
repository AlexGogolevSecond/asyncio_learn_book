import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=7432,
                                       user='alex',
                                       database='products',
                                       password='614007')

    query = 'SELECT product_id, product_name FROM product'
    async with connection.transaction():  # обязательно д.б. транзакция
        async for product in connection.cursor(query):  # выбираем по 50 (по умолчанию https://magicstack.github.io/asyncpg/current/api/index.html)
            print(product)

    await connection.close()

# тут непонятно - получается, используя async for мы не загоняем в память все результаты запроса,
# а получаем их по 50
asyncio.run(main())
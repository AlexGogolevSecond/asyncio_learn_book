import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=7432,
                                       user='alex',
                                       database='products',
                                       password='614007')

    query = 'SELECT product_id, product_name FROM product'
    async with connection.transaction():
        async for product in connection.cursor(query):  # выбираем по одному
            print(product)

    await connection.close()

# тут непонятно - получается, используя async for мы не загоняем в память все результаты запроса,
# а получаем их по одному
asyncio.run(main())
import asyncpg
import asyncio
from connection import DATABASE_URL


async def main():
    connection = await asyncpg.connect(**DATABASE_URL)

    async with connection.transaction():
        query = 'SELECT product_id, product_name from product'
        cursor = await connection.cursor(query)

        await cursor.forward(500)
        products = await cursor.fetch(100)
        for product in products:
            print(product)

    await connection.close()


asyncio.run(main())

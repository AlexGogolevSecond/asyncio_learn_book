import asyncio
import asyncpg
from connection import DATABASE_URL


async def main():
    connection = await asyncpg.connect(**DATABASE_URL)
    async with connection.transaction():  # A
        await connection.execute("INSERT INTO brand "
                                 "VALUES(DEFAULT, 'brand_1')")
        await connection.execute("INSERT INTO brand "
                                 "VALUES(DEFAULT, 'brand_2')")

    query = """SELECT brand_name FROM brand
                WHERE brand_name LIKE 'brand%'"""
    brands = await connection.fetch(query)  # B
    print(brands)

    await connection.close()


asyncio.run(main())

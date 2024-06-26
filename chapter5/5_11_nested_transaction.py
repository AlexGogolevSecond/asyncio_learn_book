import asyncio
import asyncpg
import logging
from connection import DATABASE_URL


async def main():
    connection = await asyncpg.connect(**DATABASE_URL)
    async with connection.transaction():
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'my_new_brand')")

        try:
            async with connection.transaction():
                await connection.execute("INSERT INTO product_color VALUES(1, 'black')")
        except Exception as ex:
            logging.warning('Ignoring error inserting product color', exc_info=ex)

    await connection.close()


asyncio.run(main())
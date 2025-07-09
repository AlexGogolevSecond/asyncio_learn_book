import asyncpg
import asyncio
from asyncpg import Record
from typing import List
from connection import DATABASE_URL


async def main():
    connection = await asyncpg.connect(**DATABASE_URL)
    
    # await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
    # await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")
    
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    results: List[Record] = await connection.fetch(brand_query)  # выбирает все записи
    
    if not results:
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")
    results: List[Record] = await connection.fetch(brand_query)  # выбирает все записи
    print(f'{results=}')
    for brand in results:
        print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')

    await connection.close()

asyncio.run(main())

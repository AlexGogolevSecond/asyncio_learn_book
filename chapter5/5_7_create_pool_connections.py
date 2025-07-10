import asyncio
import asyncpg
import time
from connection import DATABASE_URL


PRODUCT_QUERY = """
    SELECT
    p.product_id,
    p.product_name,
    p.brand_id,
    s.sku_id,
    pc.product_color_name,
    ps.product_size_name
    FROM product as p
    JOIN sku as s on s.product_id = p.product_id
    JOIN product_color as pc on pc.product_color_id = s.product_color_id
    JOIN product_size as ps on ps.product_size_id = s.product_size_id
    WHERE p.product_id = 175
"""


async def query_product(pool):
    async with pool.acquire() as connection:  # pool.acquire() - захват подключения из пула
        return await connection.fetchrow(PRODUCT_QUERY)


async def main():
    async with asyncpg.create_pool(**DATABASE_URL,
                                   min_size=6,
                                   max_size=6
                                   ) as pool:  # !!!!! тут двоеточие, это контекстный менеджер
        start = time.perf_counter()

        # res = await query_product(pool)
        # res = await query_product(pool)
        # res = await query_product(pool)


        res = await asyncio.gather(query_product(pool),
                                   query_product(pool),
                                   query_product(pool))

        finish = time.perf_counter()
        print(res)
        print(f'time: {finish - start}')


asyncio.run(main())

import asyncio
import asyncpg
import time
from connection import DATABASE_URL


product_query = \
"""
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
WHERE p.product_id = 175"""


async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


async def query_products_synchronously(pool, queries):
    return [await query_product(pool) for _ in range(queries)]


async def query_products_concurrently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)


async def main():
    async with asyncpg.create_pool(**DATABASE_URL,
                                   min_size=6,
                                   max_size=26) as pool:
        st1 = time.perf_counter()
        await query_products_synchronously(pool, 10000)
        print(f'синхронно: {time.perf_counter() - st1}')
        st2 = time.perf_counter()
        await query_products_concurrently(pool, 10000)
        print(f'асинхронно: {time.perf_counter() - st2}')

asyncio.run(main())

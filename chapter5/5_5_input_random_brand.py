import asyncpg
import asyncio
from typing import List, Tuple, Union, Optional
from random import sample
import os
from util.utils import load_common_words



def generate_brand_names(words: List[str]) -> List[Tuple[Optional[str]]]:
    res = [(words[index].replace('n', '').strip(),) for index in sample(range(100), 100)]
    return res


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_brands, brands)


async def main():
    common_words = load_common_words()
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=7432,
                                       user='alex',
                                       database='products',
                                       password='614007')
    await insert_brands(common_words, connection)
    await connection.close()


asyncio.run(main())

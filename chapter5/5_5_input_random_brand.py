import asyncpg
import asyncio
from typing import List, Tuple, Union, Optional
from random import sample
import os


def load_common_words() -> List[str]:
    file_name = 'common_words.txt'
    current_folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_folder, f'{file_name }')

    with open(file_path, 'r', encoding='utf-8') as common_words:
        return common_words.readlines()


def generate_brand_names(words: List[str]) -> List[Tuple[Optional[str]]]:
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_brands, brands)


async def main():
    common_words = load_common_words()
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='alex',
                                       database='products',
                                       password='614007')
    # await insert_brands(common_words, connection)
    await connection.close()


asyncio.run(main())

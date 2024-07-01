import asyncio
import asyncpg
from random import randint, sample
from typing import List, Tuple
import os
from connection import DATABASE_URL



def load_common_words() -> List[str]:
    """Читаем файл с словами и помещаем слова в список"""
    file_name = 'common_words.txt'
    current_folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_folder, f'{file_name }')

    with open(file_path, 'r', encoding='utf-8') as common_words:
        return common_words.readlines()


async def gen_products(connection,
                 common_words: List[str],
                 brand_id_start: int,
                 brand_id_end: int,
                 count_products_to_create: int) -> List[Tuple[str, int]]:
    """
    Генерируем список кортежей, состоящих из строки (10 слов) и brand_id для заполнения таблицы brand
    параметры brand_id_start и brand_id_end игнорируются
    """

    # не будем завязываться на переданны параметры brand_id_start и brand_id_end - получим
    # их из БД

    query = '''
        SELECT 
            MIN(brand_id),
            MAX(brand_id)
        FROM brand
    '''

    min_brand_id, max_brand_id = await connection.fetchrow(query)

    if all([min_brand_id, max_brand_id]):
        brand_id_start, brand_id_end = min_brand_id, max_brand_id

    products = []
    # brand_ids = []
    for _ in range(count_products_to_create):
        # в description будет 10 слов
        description = [common_words[index].replace('\n', '').strip() for index in sample(range(1000), 10)]

        brand_id = randint(brand_id_start, brand_id_end)
        # while brand_id in brand_ids:
        #     brand_id = randint(brand_id_start, brand_id_end)

        products.append((" ".join(description), brand_id))

    return products


async def gen_skus(connection,
                   product_id_start: int,
                   product_id_end: int,
                   skus_to_create: int) -> List[Tuple[int, int, int]]:
    """
    Генерируем список кортежей для заполнения таблицы sku
    параметры product_id_start и product_id_end игнорируются
    """

    # также переделываем на получение параметров product_id_start и product_id_end
    # из sql-запроса

    query = '''
        SELECT 
            MIN(product_id),
            MAX(product_id)
        FROM product
    '''

    min_product_id, max_product_id = await connection.fetchrow(query)

    if all([min_product_id, max_product_id]):
        product_id_start, product_id_end = min_product_id, max_product_id

    # т.е. чтобы не париться по поводу ИД'шников product_id - мы их получаем из БД

    skus = []
    for _ in range(skus_to_create):
        product_id = randint(product_id_start, product_id_end)
        size_id = randint(1, 3)
        color_id = randint(1, 2)
        skus.append((product_id, size_id, color_id))

    return skus


async def main():
    common_words = load_common_words()
    connection = await asyncpg.connect(**DATABASE_URL)

    product_tuples: List[Tuple[str, int]] = await gen_products(connection,
                                                               common_words,
                                                               brand_id_start=105,
                                                               brand_id_end=204,
                                                               count_products_to_create=1000)

    await connection.executemany("INSERT INTO product VALUES(DEFAULT, $1, $2)", product_tuples)

    sku_tuples = await gen_skus(connection,
                                product_id_start=2,
                                product_id_end=1001,
                                skus_to_create=100000)

    await connection.executemany("INSERT INTO sku VALUES(DEFAULT, $1, $2, $3)", sku_tuples)
    await connection.close()


asyncio.run(main())

import asyncio
import asyncpg
from asyncpg.transaction import Transaction  # нужно только для указания типа для переменной transaction
from connection import DATABASE_URL


async def main():
    connection = await asyncpg.connect(**DATABASE_URL)
    transaction: Transaction = connection.transaction()  # создаем объект транзакции, но без контекстного менеджера
    await transaction.start()

    try:
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_1')")
        await connection.execute("INSERT INTO brand23232 VALUES(DEFAULT, 'brand_2')")
    except asyncpg.PostgresError:
        print('Ошибка, транзакция откатывается!')
        await transaction.rollback()
    else:
        print('Транзакция успешно завершена!')
        await transaction.commit()

    query = """select brand_name from brand
               where brand_name LIKE 'brand%'"""
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()

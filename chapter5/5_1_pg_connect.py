import asyncpg
import asyncio

from connection import DATABASE_URL


async def main():
    connection = await asyncpg.connect(**DATABASE_URL)
    version = connection.get_server_version()
    print(f'Подключено! Версия Postgres равна {version}')
    await connection.close()

asyncio.run(main())

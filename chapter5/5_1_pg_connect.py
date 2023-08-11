import asyncpg
import asyncio


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='alex',
                                       database='postgres',
                                       password='614007')
    version = connection.get_server_version()
    print(f'Подключено! Версия Postgres равна {version}')
    await connection.close()

asyncio.run(main())

# Создание и уничтожение пула подключений к базе данных
import asyncpg
from aiohttp.web_app import Application
from asyncpg.pool import Pool
from chapter5.connection import DATABASE_URL

DB_KEY = 'database'


async def create_database_pool(app: Application, database: str):
    # Копируем DATABASE_URL, чтобы не менять оригинал
    db_url = DATABASE_URL.copy()
    # Удаляем ключ 'database', если он есть
    db_url.pop('database', None)
    pool: Pool = await asyncpg.create_pool(
        database=database,
        min_size=6,
        max_size=60,
        **db_url
    )
    app[DB_KEY] = pool


async def destroy_database_pool(app: Application):
    pool: Pool = app[DB_KEY]
    await pool.close()

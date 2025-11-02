import asyncpg
from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool
from typing import List, Dict

from chapter5.connection import DATABASE_URL

routes = web.RouteTableDef()
DB_KEY = 'database'


async def create_database_pool(app: Application): #A
    print('Creating database pool.')
    # pool: Pool = await asyncpg.create_pool(host='127.0.0.1',
    #                                        port=5432,
    #                                        user='postgres',
    #                                        password='password',
    #                                        database='products',
    #                                        min_size=6,
    #                                        max_size=6)

    pool: Pool = await asyncpg.create_pool(
        min_size=30,           # Компромиссный вариант
        max_size=200,           # Чуть меньше максимума
        max_inactive_connection_lifetime=60,
        command_timeout=30,    # Таймаут на запросы
        **DATABASE_URL)
    
    # !!! в постгрес поменял значение max_connections = 500 и перезапустил докер контейнер с постгресом

    app[DB_KEY] = pool


async def destroy_database_pool(app: Application): #B
    print('Destroying database pool.')
    pool: Pool = app[DB_KEY]
    await pool.close()


@routes.get('/brands')
async def brands(request: Request) -> Response: #C
    pool: Pool = request.app[DB_KEY]
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    results: List[Record] = await pool.fetch(brand_query)
    result_as_dict: List[Dict] = [dict(brand) for brand in results]
    return web.json_response(result_as_dict)


app = web.Application()
app.on_startup.append(create_database_pool)  # сопрограмма create_database_pool выполняется при запуске приложения; on_startup - обработчик сигнала
app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
# web.run_app(app, access_log=None, print=None)  # убрал, т.к. запускаю через gunicorn -w 8 -k aiohttp.GunicornWebWorker -b localhost:8080 chapter9.listing_9_2_connect_to_postgres:app

# запуск скрипта: (env) alex@ubuntu-home:~/py_tmp/asyncio_learn_book$ python -m chapter9.listing_9_2_connect_to_postgres.py
# в этом случае корректно распознаются абсолютные пути - в данном случае для получения параметров из DATABASE_URL

'''
Вывод:
wrk -t1 -c200 -d30s http://localhost:8080/brands
Running 30s test @ http://localhost:8080/brands
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   143.45ms  117.69ms   1.11s    64.93%
    Req/Sec     1.55k   135.65     1.83k    77.67%
  46205 requests in 30.03s, 179.43MB read
Requests/sec:   1538.81
Transfer/sec:      5.98MB

тут на одном процессе в одном потоке 1500 рпс, а на фласке с 4-мя процессами 3000 рпс. Хотя на фласке в htop почему то
задействуются все 8 ядер, хотя я указывал гуникорну 4 ядра. На 8 ядрах у фласка 4000 рпс.
'''

# на ноуте в wsl:
# один проесс - капец медленно
# wrk -t1 -c200 -d30s http://localhost:8080/brands
# Running 30s test @ http://localhost:8080/brands
#   1 threads and 200 connections
#   Thread Stats   Avg      Stdev     Max   +/- Stdev
#     Latency   151.30ms  251.44ms   1.99s    95.27%
#     Req/Sec     2.01k   361.52     2.43k    90.18%
#   57291 requests in 28.38s, 222.59MB read
#   Socket errors: connect 0, read 0, write 0, timeout 218
# Requests/sec:   2018.49
# Transfer/sec:      7.84MB

# 8 процессов/воркеров (гуникорн):
# wrk -t1 -c200 -d30s http://localhost:8080/brands
# Running 30s test @ http://localhost:8080/brands
#   1 threads and 200 connections
#   Thread Stats   Avg      Stdev     Max   +/- Stdev
#     Latency    43.17ms   39.02ms   1.53s    81.85%
#     Req/Sec     4.84k   785.34     6.28k    68.00%
#   145063 requests in 29.18s, 563.61MB read
#   Socket errors: connect 0, read 0, write 0, timeout 345
# Requests/sec:   4971.51
# Transfer/sec:     19.32MB



# Конфигурация	Req/Sec	Прирост vs Flask
# Flask + gunicorn	4027	базовый
# aiohttp + gunicorn (min=50)	4426	+10%
# aiohttp + gunicorn (min=30)	4971	+23%
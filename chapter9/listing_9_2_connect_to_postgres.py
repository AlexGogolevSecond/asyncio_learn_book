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

    pool: Pool = await asyncpg.create_pool(min_size=6,
                                           max_size=6,
                                           **DATABASE_URL)

    app[DB_KEY] = pool


async def destroy_database_pool(app: Application): #B
    print('Destroying database pool.')
    pool: Pool = app[DB_KEY]
    await pool.close()


@routes.get('/brands')
async def brands(request: Request) -> Response: #C
    connection: Pool = request.app[DB_KEY]
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    results: List[Record] = await connection.fetch(brand_query)
    result_as_dict: List[Dict] = [dict(brand) for brand in results]
    return web.json_response(result_as_dict)


app = web.Application()
app.on_startup.append(create_database_pool)  # сопрограмма create_database_pool выполняется при запуске приложения; on_startup - обработчик сигнала
app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
web.run_app(app)

# запуск скрипта: (env) alex@ubuntu-home:~/py_tmp/asyncio_learn_book$ python -m chapter9._9_2_connect_to_postgres.py
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
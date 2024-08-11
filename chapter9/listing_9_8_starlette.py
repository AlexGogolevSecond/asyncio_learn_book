import asyncpg
from asyncpg import Record
from asyncpg.pool import Pool
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route
from typing import List, Dict


async def create_database_pool():
    pool: Pool = await asyncpg.create_pool(host='127.0.0.1',
                                           port=19432,
                                           user='postgres',
                                           password='password',
                                           database='products',
                                           min_size=6,
                                           max_size=6)
    app.state.DB = pool


async def destroy_database_pool():
    pool = app.state.DB
    await pool.close()


async def brands(request: Request) -> Response:
    connection: Pool = request.app.state.DB
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    results: List[Record] = await connection.fetch(brand_query)
    result_as_dict: List[Dict] = [dict(brand) for brand in results]
    return JSONResponse(result_as_dict)


app = Starlette(routes=[Route('/brands', brands)],
                on_startup=[create_database_pool],
                on_shutdown=[destroy_database_pool])


# uvicorn --workers 8 --log-level error chapter9.listing_9_8_starlette:app

'''
wrk -t1 -c200 -d30s http://localhost:8000/brands
Running 30s test @ http://localhost:8000/brands
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    55.80ms    9.08ms 256.05ms   86.43%
    Req/Sec     3.59k   244.88     4.09k    84.33%
  107158 requests in 30.03s, 372.00MB read
Requests/sec:   3568.03
Transfer/sec:     12.39MB
'''


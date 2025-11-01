import asyncpg
from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool
from chapter5.connection import DATABASE_URL


routes = web.RouteTableDef()
DB_KEY = 'database'


@routes.get('/products/{id}')
async def get_product(request: Request) -> Response:
    try:
        str_id = request.match_info['id'] #A
        product_id = int(str_id)

        query = """
            SELECT
                product_id,
                product_name,
                brand_id
            FROM product
            WHERE product_id = $1
        """

        connection: Pool = request.app[DB_KEY]
        result: Record = await connection.fetchrow(query, product_id) #B

        if result is not None: #C
            return web.json_response(dict(result))
        else:
            raise web.HTTPNotFound()  # 404
    except ValueError:
        raise web.HTTPBadRequest()  # 400


async def create_database_pool(app: Application):
    print('Creating database pool.')
    pool: Pool = await asyncpg.create_pool(min_size=6,
                                           max_size=6,
                                           **DATABASE_URL)
    app[DB_KEY] = pool


async def destroy_database_pool(app: Application):
    print('Destroying database pool.')
    pool: Pool = app[DB_KEY]
    await pool.close()


app = web.Application()
app.on_startup.append(create_database_pool)
app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
web.run_app(app)

# запуск скрипта: (env) alex@ubuntu-home:~/py_tmp/asyncio_learn_book$ python -m chapter9.9_3_get_product_by_id.py
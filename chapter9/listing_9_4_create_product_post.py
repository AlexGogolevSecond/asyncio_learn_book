from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from chapter9.listing_9_2_connect_to_postgres import create_database_pool, destroy_database_pool
from asyncpg.pool import Pool
from asyncpg import Record


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

@routes.post('/product')
async def create_product(request: Request) -> Response:
    PRODUCT_NAME = 'product_name'
    BRAND_ID = 'brand_id'

    print(f'{request.text=}')
    if not request.can_read_body:
        raise web.HTTPBadRequest()

    body = await request.json()

    if PRODUCT_NAME in body and BRAND_ID in body:
        db = request.app[DB_KEY]
        await db.execute('''INSERT INTO product(product_id,
                                                product_name, 
                                                brand_id) 
                                                VALUES(DEFAULT, $1, $2)''',
                         body[PRODUCT_NAME],
                         int(body[BRAND_ID]))
        return web.Response(status=201)
    else:
        raise web.HTTPBadRequest(text='Какая-то ерунда в теле запроса!')


app = web.Application()
app.on_startup.append(create_database_pool)
app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
web.run_app(app, port=50000)
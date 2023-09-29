import asyncio
import asyncpg


query = '''
    with wares as (
        select
            product.product_id,
            product.product_name,
            brand.brand_name
        from product
        left join brand on product.brand_id = brand.brand_id
    )
    select
        sku.sku_id,
        wares.product_id,
        wares.product_name,
        wares.brand_name,
        product_color.product_color_name,
        product_size.product_size_name 
    from wares
    left join sku on sku.product_id  = wares.product_id
    left join product_color on sku.product_color_id  = product_color.product_color_id 
    left join product_size on sku.product_size_id = product_size.product_size_id 
'''


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=7432,
                                       user='alex',
                                       database='products',
                                       password='614007')
    
    result = await connection.fetch(query)
    a = 0


asyncio.run(main())

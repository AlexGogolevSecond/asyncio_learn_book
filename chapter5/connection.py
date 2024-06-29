host='127.0.0.1'
port=19432
user='postgres'
database='products'
password='password'

# DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}'  # почему-то не робит в 5_3
DATABASE_URL = {'host': '127.0.0.1',
                 'port': 19432,
                 'user': 'postgres',
                 'database': 'products',
                 'password': 'password'
                }

host='172.17.188.173'  # '127.0.0.1'  # '172.17.188.173'
port=5432
user='postgres'
database='products'
password='password'



# DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}'  # почему-то не робит в 5_3
DATABASE_URL = {'host': host,
                'port': port,
                'user': user,
                'database': database,
                'password': password
}

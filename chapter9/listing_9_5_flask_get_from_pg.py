from flask import Flask, jsonify
import psycopg2
from chapter5.connection import DATABASE_URL

app = Flask(__name__)

conn_info = "dbname=products user=postgres password=password host=127.0.0.1 port=6432"
db = psycopg2.connect(conn_info)


@app.route('/brands')
def brands():
    cur = db.cursor()
    cur.execute('SELECT brand_id, brand_name FROM brand')
    rows = cur.fetchall()
    cur.close()
    return jsonify([{'brand_id': row[0], 'brand_name': row[1]} for row in rows])

# запуск Flask приложения (этого питонячего модуля) с помощью gunicorn: gunicorn -w 8 chapter9.listing_9_5_flask_get_from_pg:app 
# нагрузочный тест:
# wrk -t1 -c200 -d30s http://localhost:8000/brands - в теч. 30 с. в одном потоке 200 подключений 


# Вывод:
# wrk -t1 -c200 -d30s http://localhost:8000/brands
# Running 30s test @ http://localhost:8000/brands
#   1 threads and 200 connections
#   Thread Stats   Avg      Stdev     Max   +/- Stdev
#     Latency    63.09ms    4.04ms 106.76ms   96.69%
#     Req/Sec     3.17k   159.12     3.36k    95.00%
#   94678 requests in 30.01s, 330.56MB read
# Requests/sec:   3154.57
# Transfer/sec:     11.01MB

# на ноуте:
# flask:
# alex@hp-laptop:~$ wrk -t1 -c200 -d30s http://localhost:8000/brands
# Running 30s test @ http://localhost:8000/brands
#   1 threads and 200 connections
#   Thread Stats   Avg      Stdev     Max   +/- Stdev
#     Latency    52.27ms    9.72ms 158.81ms   88.97%
#     Req/Sec     3.82k   583.95     4.80k    80.60%
#   114327 requests in 28.39s, 399.16MB read
#   Socket errors: connect 0, read 0, write 0, timeout 200
# Requests/sec:   4027.62
# Transfer/sec:     14.06MB

# aiohttp:
# на ноуте в wsl:
# wrk -t1 -c200 -d30s http://localhost:8080/brands
# Running 30s test @ http://localhost:8080/brands
#   1 threads and 200 connections
#   Thread Stats   Avg      Stdev     Max   +/- Stdev
#     Latency   120.33ms   45.90ms 635.07ms   83.99%
#     Req/Sec     1.69k   310.30     2.05k    85.95%
#   50531 requests in 28.41s, 196.33MB read
#   Socket errors: connect 0, read 0, write 0, timeout 200
# Requests/sec:   1778.93
# Transfer/sec:      6.91MBB

# 8 процессов/воркеров (гуникорн) aiohttp:
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

# 
# Конфигурация	Req/Sec	Прирост vs Flask
# Flask + gunicorn	4027	базовый
# aiohttp + gunicorn (min=50)	4426	+10%
# aiohttp + gunicorn (min=30)	4971	+23%

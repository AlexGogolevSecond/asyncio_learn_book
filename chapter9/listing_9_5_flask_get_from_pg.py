from flask import Flask, jsonify
import psycopg2
from chapter5.connection import DATABASE_URL

app = Flask(__name__)

conn_info = "dbname=products user=postgres password=password host=127.0.0.1 port=19432"
db = psycopg2.connect(DATABASE_URL)


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

'''
Вывод:
wrk -t1 -c200 -d30s http://localhost:8000/brands
Running 30s test @ http://localhost:8000/brands
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    63.09ms    4.04ms 106.76ms   96.69%
    Req/Sec     3.17k   159.12     3.36k    95.00%
  94678 requests in 30.01s, 330.56MB read
Requests/sec:   3154.57
Transfer/sec:     11.01MB

''' 

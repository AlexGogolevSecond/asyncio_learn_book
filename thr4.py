import requests
import threading
from time import perf_counter


sources = ["https://ya.ru",
           "https://www.bing.com",
           "https://www.google.ru",
           "https://www.yahoo.com",
           "https://mail.ru"]

headers_stor = {}  # Храним здесь заголовки


def get_request_header(url: str):
    headers_stor[url] = requests.get(url).headers


start = perf_counter()
sum_ex_time = 0
threads = []
delays = []

for source in sources:
    # start_tmp = perf_counter()
    thr = threading.Thread(target=get_request_header, args=(source,))
    threads.append(thr)
    thr.start()
    # # thr.join()
    # delta = perf_counter() - start_tmp
    # delays.append(delta)
    # print(source, delta)
    # sum_ex_time += delta

for thr in threads:
    # thr.start()
    thr.join(1.5)

headers_stor = {x: headers_stor.get(x, 'no_response') for x in sources}


print(f"completed in {perf_counter() - start} seconds")  # Считаем общее время выполнения всех запросов
# print(sum_ex_time)  # Показываем то, что общее время работы является простой суммой каждого запроса по отдельности
print(*headers_stor.items(), sep="\n")  # Выводим наши заголовки

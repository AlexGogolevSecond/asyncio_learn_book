import time
import requests
from concurrent.futures import ThreadPoolExecutor


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


start = time.time()

with ThreadPoolExecutor(max_workers=700) as pool:
    urls = ['https://www.example.com' for _ in range(1000)]
    results = pool.map(get_status_code, urls)
    # for result in results:
    #     print(result)
# синхронный вариант:
# urls = ['https://www.example.com' for _ in range(1000)]
# for url in urls:
#     get_status_code(url)

end = time.time()

print(f'finished requests in {end - start:.4f} second(s)')

# по умолчанию max_workers = min(32, os.cpu_count() + 4), т.е. если 8 ядер, то 12 воркеров: finished requests in 36.4216 second(s)
# вывод:
# при 1000 воркерах: finished requests in 2.5712 second(s)
# при 10 воркерах: finished requests in 28.3595 second(s)
# при 4-х воркерах:finished requests in 142.1162 second(s)
# при 500 воркерах: finished requests in 2.2910 second(s)
# при 2000 воркеров: finished requests in 136.0668 second(s)
# при 100 воркерах: finished requests in 3.6279 second(s)

import time
from concurrent.futures import ProcessPoolExecutor


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
    end = time.time()
    print(f'Закончен подсчет до {count_to} за время {end - start}')
    return counter


if __name__ == "__main__":
    st = time.perf_counter()
    with ProcessPoolExecutor() as process_pool:
        numbers = [100_000_000, 1, 3, 5, 22]
        for result in process_pool.map(count, numbers):
            print(result)
    print(f'итого: {time.perf_counter() - st}')

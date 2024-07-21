import time
from multiprocessing import Process


def count(count_to: int) -> int:
    start = time.perf_counter()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.perf_counter()
    print(f'Закончен подсчет до {count_to} за время {end-start}')

    return counter


if __name__ == "__main__":
    start_time = time.perf_counter()
    to_one_hundred_million = count(100_000_000)
    to_two_hundred_million = count(200_000_000)

    # print('lalala')
    end_time = time.perf_counter()
    print(f'Полное время работы {end_time-start_time}')

"""
Вывод:

Закончен подсчет до 100000000 за время 18.42056828099976
Закончен подсчет до 200000000 за время 36.009021460999975
Полное время работы 54.42975734799984
"""
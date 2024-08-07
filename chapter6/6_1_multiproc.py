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
    to_one_hundred_million = Process(target=count, args=(100_000_000,))
    to_two_hundred_million = Process(target=count, args=(200_000_000,))

    to_one_hundred_million.start()
    to_two_hundred_million.start()

    to_one_hundred_million.join()
    to_two_hundred_million.join()
    print('lalala')
    end_time = time.perf_counter()
    print(f'Полное время работы {end_time-start_time}')

"""
Вывод:

Закончен подсчет до 100000000 за время 17.696253221000006
Закончен подсчет до 200000000 за время 34.22645878500043
lalala
Полное время работы 35.85876596900016

"""

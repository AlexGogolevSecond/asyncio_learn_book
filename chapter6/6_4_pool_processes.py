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
        numbers = [100_000_000, 1, 3, 5, 22, 200_000_000]
        for result in process_pool.map(count, numbers):
            print(f'{result=}')
    print(f'итого: {time.perf_counter() - st}')

'''
Закончен подсчет до 3 за время 9.5367431640625e-07
Закончен подсчет до 5 за время 9.5367431640625e-07
Закончен подсчет до 1 за время 1.6689300537109375e-06
Закончен подсчет до 22 за время 2.86102294921875e-06
Закончен подсчет до 100000000 за время 3.611050605773926
result=100000000
result=1
result=3
result=5
result=22
Закончен подсчет до 200000000 за время 7.353483200073242
result=200000000
итого: 7.37034298800063
'''

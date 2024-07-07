from multiprocessing import Pool
import time


def say_hello(name: str) -> str:
    return f'Привет, {name}'


def count(count_to: int) -> int:
    start = time.perf_counter()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.perf_counter()
    print(f'Закончен подсчет до {count_to} за время {end-start}')

    return counter


if __name__ == "__main__":
    st = time.perf_counter()
    with Pool() as process_pool:
        # hi_jeff = process_pool.apply(say_hello, args=('Jeff',))
        # hi_john = process_pool.apply(say_hello, args=('John',))
        # print(hi_jeff)
        # print(hi_john)
        p1 = process_pool.apply(count, args=(100_000_000,))  # НО, метод apply блокирующий, поэтому не подходит - робит синхронно
        p2 = process_pool.apply(count, args=(200_000_000,))
        print(f'{p1=}')
        print(f'{p2=}')
    
    print(time.perf_counter() - st)


"""
Вывод:

Закончен подсчет до 100000000 за время 16.953953226999147
Закончен подсчет до 200000000 за время 33.63915000400084
p1=100000000
p2=200000000
51.07165664000058

"""
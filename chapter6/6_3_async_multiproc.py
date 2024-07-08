from multiprocessing import Pool
import time


def say_hello(name: str) -> str:
    return f'Привет, {name}'


def count(count_to: int) -> int:
    start = time.perf_counter()
    counter = 0
    while counter < count_to:
        counter = counter + 1
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
        p1 = process_pool.apply_async(count, args=(100_000_000,))
        p2 = process_pool.apply_async(count, args=(20_000_000,))
        p3 = process_pool.apply_async(count, args=(40_000_000,))
        p4 = process_pool.apply_async(count, args=(20_000_000,))
        p5 = process_pool.apply_async(count, args=(30_000_000,))
        # почему-то без принтов сразу сбрасывается, как будто нет join по процессам и главный процесс никого не ждёт
        # ответ ниже

        # print(f'type(p1): {type(p1)}')  # тут вернётся class 'multiprocessing.pool.ApplyResult'
        # метод get у ApplyResult возвращает результат
        print(f'{p1.get()=}')
        print(f'{p2.get()=}')
        print(f'{p3.get()=}')
        print(f'{p4.get()=}')
        print(f'{p5.get()=}')
    
    print(time.perf_counter() - st)

    # ну так себе - пользоваться таким неудобно
    # или загонять все p1,... в список и уже его потом обходить и получать по каждому get


"""
Вывод:

Закончен подсчет до 20000000 за время 5.413807672000075
Закончен подсчет до 20000000 за время 5.408814813999925
Закончен подсчет до 30000000 за время 7.85565982099979
Закончен подсчет до 40000000 за время 9.817661207999663
Закончен подсчет до 100000000 за время 21.813264616000197
p1.get()=100000000
p2.get()=20000000
p3.get()=40000000
p4.get()=20000000
p5.get()=30000000
22.27775255800043

"""
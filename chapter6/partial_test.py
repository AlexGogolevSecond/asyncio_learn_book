'''
Метод partial позволяет заменять метод с параметрами на метод без параметров
Например, нужно для асинхронного запуска процессов в eventloop'е в asyncio
'''

from functools import partial


def count(num: int) -> int:
    counter = 0
    while counter < num:
        counter += 1
    return counter

f = partial(count, 555)
res = f()
a = 0
print(res)


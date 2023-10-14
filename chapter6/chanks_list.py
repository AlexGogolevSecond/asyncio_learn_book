from typing import List


def partition(data: List, chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        print(f'i: {i}')
        yield data[i:i + chunk_size]



l = list(range(100))

a = partition(l, 4)

for i in a:
    print(i)

b = 0

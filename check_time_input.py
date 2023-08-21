from time import perf_counter


def input_list(n):
    start = perf_counter()
    l = list(range(10000000))
    l.append(n)
    print(perf_counter() - start)


def input_list_begin(n):
    start = perf_counter()
    l = list(range(10000000))
    l.insert(0, n)
    print(perf_counter() - start)

input_list(5)
input_list_begin(5)

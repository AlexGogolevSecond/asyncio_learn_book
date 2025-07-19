from multiprocessing import Process, Value, cpu_count
import os


def increment_value(shared_int: Value):
    print(f'{os.getpid()=}')
    shared_int.value = shared_int.value + 1
    print(f'{shared_int.value=}')


if __name__ == '__main__':
    print(f'{cpu_count()=}')
    for _ in range(10):
        integer = Value('i', 0)
        procs = [Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,))]

        [p.start() for p in procs]
        [p.join() for p in procs]
        print(f'{integer.value=}')
        assert(integer.value == 2)

# но тут состояние гонки
from multiprocessing import Process, Value, cpu_count


def increment_value(shared_int: Value):
    shared_int.get_lock().acquire()  # захватываем блокировку
    shared_int.value = shared_int.value + 1
    shared_int.get_lock().release()  # освобождение блокировки
    # НО такой подход делает код синхронным

    # # наверное лучше использовать контекстный менеджер
    # with shared_int.get_lock():
    #     shared_int.value = shared_int.value + 1

if __name__ == '__main__':
    print(f'{cpu_count()=}')
    for j in range(10):
        print(f'{j=}')
        integer = Value('i', 0)
        procs = [Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,))]

        [p.start() for p in procs]
        [p.join() for p in procs]
        print(f'{integer.value=}')
        assert (integer.value == 2)
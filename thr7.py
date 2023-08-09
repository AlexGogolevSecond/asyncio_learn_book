import threading
from time import sleep, perf_counter


def task(n):
    print(f"-starting task with {threading.current_thread().name}, {threading.active_count()=}")
    sleep(n)
    print(f"---end task with {threading.current_thread().name}")

start = perf_counter()
task(0)
thr_1 = threading.Thread(target=task, args=(3,), name='One')
thr_1.start()

thr_2 = threading.Thread(target=task, args=(2,), name='Two')
thr_2.start()

thr_3 = threading.Thread(target=task, args=(1,), name='Three')
thr_3.start()


thr_1.join()
thr_2.join()
thr_3.join()

print(f"{threading.active_count()=}")
print("END MAIN")
print(f'total: {perf_counter() - start}')

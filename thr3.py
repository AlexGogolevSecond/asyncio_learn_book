from time import sleep
import threading


def test(l: str, aaa: bool = True, t: int = 2):
    print(f'{l=}; {aaa=}; {t=}')



# thr1 = threading.Thread(target=test, args=['bbb', 5, False])
thr1 = threading.Thread(target=test, kwargs={'l': 'ssss'})
thr1.start()


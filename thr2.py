import threading
import time


def req_to():
    # return requests.get("https://www.state.gov/countries-areas/chile/").status_code
    time.sleep(3)

st = time.monotonic()
t1 = threading.Thread(target=req_to)
t1.start()

t2 = threading.Thread(target=req_to)
t2.start()

print(f'Name current thread: {threading.current_thread().name}')
t1.join()
t2.join()
fin = time.monotonic()
delta = fin - st
print(f'delta: {delta}')






    

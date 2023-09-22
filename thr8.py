import threading
import requests
import time




def get_status(url):
    return requests.get(url).status_codes_code


def main():
    url = 'https://profi-leader.com/'
    urls = [url for _ in range(1000)]
    for url in urls:
        threading.Thread(target=get_status, args=(url,), name='One')


if __name__ == '__main__':
    st = time.perf_counter()    
    main()
    print(time.perf_counter() - st)



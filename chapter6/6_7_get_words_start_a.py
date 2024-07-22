import time
import os

file_size = os.path.getsize('chapter6/googlebooks-eng-all-1gram-20120701-a')  # 1.68 Gb
print(f'Размер файла: {file_size} байт ({round((file_size / (1024*1024*1024)), 2)} Гбайт)')

st1 = time.time()
freqs = {}
with open('chapter6/googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
    lines = f.readlines()  # это точно оптимально? - нет, но приходится так делать (хотя можно расмотреть вариант с yield)
    start = time.time()
    for line in lines:
        data = line.split('\t')
        word = data[0]
        count = int(data[2])
        if word in freqs:
            freqs[word] += count
        else:
            freqs[word] = count
    end = time.time()

    print(f'{end-start:.2f} c.')
    print(f'{end-st1:.2f} c. - вместе с загрузкой всех строк в память')

'''
Нужный нам файл можно скачать по адресу https://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-a.gz
или https://mattfowler.io/data/googlebooks-eng-all-1gram-20120701-a.gz. Любую другую часть
этого набора данных можно скачать по адресу http://storage.googlea-pis.com/books/ngrams/books/datasetsv2.html

Вывод:
Размер файла: 1801526075 байт (1.68 Гбайт)
50.95 c.
57.88 c. - вместе с загрузкой всех строк в память

'''


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
'''
Файл содержит:

A'Aang_NOUN	1879	45	5
A'Aang_NOUN	1882	5	4
A'Aang_NOUN	1885	1	1
A'Aang_NOUN	1891	1	1
A'Aang_NOUN	1899	20	4
A'Aang_NOUN	1927	3	1
A'Aang_NOUN	1959	5	2
A'Aang_NOUN	1962	2	2
A'Aang_NOUN	1963	1	1
A'Aang_NOUN	1966	45	13
A'Aang_NOUN	1967	6	4
A'Aang_NOUN	1968	5	4
A'Aang_NOUN	1970	6	2
A'Aang_NOUN	1975	4	1
A'Aang_NOUN	2001	1	1
A'Aang_NOUN	2004	3	1
A'que_ADJ	1808	1	1
A'que_ADJ	1849	2	1
A'que_ADJ	1850	1	1
A'que_ADJ	1852	4	3
A'que_ADJ	1854	5	3
A'que_ADJ	1856	2	1
A'que_ADJ	1858	4	3
A'que_ADJ	1862	2	1
A'que_ADJ	1871	1	1
A'que_ADJ	1872	2	2
A'que_ADJ	1873	1	1
A'que_ADJ	1874	2	2
A'que_ADJ	1875	3	3
A'que_ADJ	1877	1	1
A'que_ADJ	1881	1	1
A'que_ADJ	1883	1	1

'''

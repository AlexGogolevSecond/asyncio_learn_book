import time
import os

file_size = os.path.getsize('chapter6/googlebooks-eng-all-1gram-20120701-a')
print(f'Размер файла: {file_size} байт ({round((file_size / (1024*1024*1024)), 2)} Гбайт)')

st1 = time.time()
freqs = {}
with open('chapter6/googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
    lines = f.readlines()
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

    print(f'{end-start:.4f} c.')
    print(f'{end-st1:.4f} c.')

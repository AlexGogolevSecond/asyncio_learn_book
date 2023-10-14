import time
import os
#import pdb; pdb.set_trace()

def get_chanck(file_object, chank=2):
    while True:
        data = file_object.read(chank)
        if not data:
            break
        print(f'data: {data}')
        yield data


with open('chapter6/test_file_for_read.txt') as file:
    '''f = file.readlines()  # тут весь файл загоняется в список (по переносу строки)
    a = 0
    '''
    g = get_chanck(file)
    for i in g:
        print(i)

    '''
    # читаем по частям (побайтово)
    f = file.read(3)
    f = file.read(3)
    a = 0
    '''

'''
file_size = os.path.getsize('chapter6/googlebooks-eng-all-1gram-20120701-a')  # 1.68 Gb
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
'''

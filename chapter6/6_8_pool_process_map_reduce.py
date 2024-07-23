#https://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-a.gz
import asyncio
import concurrent.futures
import functools
import time
from typing import Dict, List


def partition(data: List, chunk_size: int):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split('\t')
        if counter.get(word):
            counter[word] = counter[word] + int(count)
        else:
            counter[word] = int(count)
    return counter


def merge_dictionaries(first: Dict[str, int], 
                       second: Dict[str, int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] += second[key]
        else:
            merged[key] = second[key]
        return merged


async def main(partition_size=60000):
    with open('chapter6/googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
        contents = f.readlines()  # нафига всё грузить в память - тут теряется смысл оптимизации, хотя вроде как сама оптимизация
        # направлена на многопро
        print(f'загрузили файл в память (как список строк); размер contents: {contents.__sizeof__()}')
        loop = asyncio.get_running_loop()
        tasks = []
        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as pool:
            for chunk in partition(contents, partition_size):
                tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))

            intermediate_results = await asyncio.gather(*tasks)  # тут ждём все процессы
            st_reduce = time.time()
            final_result = functools.reduce(merge_dictionaries, intermediate_results)
            fin_reduce = time.time()
            print(f'functools.reduce выполнился за: {fin_reduce - st_reduce}')
            # print('-' *25 )
            # print(final_result.keys())
            # print('-' *25 )
            #print(f"Aardvark встречается {final_result.get('Aardvark_')} раз.")  # AFFIX_
            print(f"AFFIX_ встречается {final_result.get('A.D.A.A.')} раз.")
            end = time.time()
            print(f'Время MapReduce: {(end - start):.4f} секунд')


if __name__ == "__main__":
    asyncio.run(main(partition_size=60000))

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
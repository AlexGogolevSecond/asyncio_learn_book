'''
def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

        
file = open('chapter6/googlebooks-eng-all-1gram-20120701-a')
res1 = file.read()  # ~ 3.35 Гб в памяти
res2 = res1.split('\n')  # разделение строки по разделителю и возврат списка из этой строки


with open('chapter6/googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
    for piece in read_in_chunks(f):
        print(piece)
'''


def file_reader(file_name):
    file = open(file_name, encoding='utf-8')
    print(f'file.__sizeof__(): {file.__sizeof__()}')
    result = file.read()
    print(f'result.__sizeof__(): {result.__sizeof__()}')
    result = result.split('\n')
    print(r'result.split(\n).__sizeof__(): {}'.format(result.__sizeof__()))
    return result


f = file_reader("chapter6/googlebooks-eng-all-1gram-20120701-a")
row_count = 0

for row in f:
    row_count += 1

print(f"Row count is {row_count}")

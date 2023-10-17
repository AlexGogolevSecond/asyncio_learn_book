import time


def csv_reader(file_name):
    # очень ресурсоёмкий метод ~ 14.5 Гб памяти отъедает
    file = open(file_name)
    result = file.read().split("\n")
    return result

def csv_reader2(file_name):  # тут примерно 100 Мб отъедает, но очень медленный - почему-то не смог дождаться окончания работы метода
    for row in open(file_name, "r"):
        yield row

st = time.perf_counter()
file = "chapter6/googlebooks-eng-all-1gram-20120701-a"
print('before csv_gen = ')
#file = "chapter6/test_file_for_read.txt"
#csv_gen = csv_reader(file)
#csv_gen = csv_reader2(file)
csv_gen = (row for row in open(file))  # более питонячее формирование выражения-генератора - аналог csv_reader2
row_count = 0

print('before circle by csv_gen')
for row in csv_gen:

    # if 'ardvark' in row.lower():
    #     a = 0
    row_count += 1
    if row_count % 1000000 == 0:
        print(f'row_count: {row_count}')

print(f'csv_reader time: {time.perf_counter() - st}')  # ресурсоёмкий метод ~ 35 сек занимает;
                                                       # метод с генераторм (или выражение-генератор) ~ 346 сек.
print(f"Row count is {row_count}")

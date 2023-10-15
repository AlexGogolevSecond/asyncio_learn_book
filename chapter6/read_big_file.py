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
csv_gen = csv_reader2("chapter6/googlebooks-eng-all-1gram-20120701-a")
#csv_gen = csv_reader2("chapter6/test_file_for_read.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f'csv_reader time: {time.perf_counter() - st}')  # ресурсоёмкий метод ~ 26 сек занимает
print(f"Row count is {row_count}")

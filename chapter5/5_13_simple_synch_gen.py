def positive_integers(until: int):
    for integer in range(until):
        yield integer


positive_iterator = positive_integers(2)  # 2_000_000_000_000 занимает 88 байт И 2 тоже занимает 88 байт
# 1-ый способ
#print(next(positive_iterator))
#print(next(positive_iterator))

# 2-й способ
for el in positive_iterator:
    print(el)

a = 0
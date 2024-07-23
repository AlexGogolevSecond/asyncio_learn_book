def part(data, part_size):
     for i in range(0, len(data), part_size):
         print(f'{i=}; {data[i: i + part_size]=}')
         yield data[i: i + part_size]


l = list(range(100))

for j in part(l, 5):
     print(f'{j=}')
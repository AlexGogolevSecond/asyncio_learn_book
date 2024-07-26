import numpy as np
import time

data_points = 400_000_000
rows = 50
columns = int(data_points / rows)

matrix = np.arange(data_points).reshape(rows, columns)

s = time.time()

res = np.mean(matrix, axis=1)

e = time.time()
print(e - s)  # 0.42987537384033203 c. (вщ го такой код выполняется за 285.690921ms)

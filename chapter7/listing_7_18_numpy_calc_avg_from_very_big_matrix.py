import numpy as np
import time

data_points = 500_000_000  # 4_000_000_000
rows = 50
columns = int(data_points / rows)

matrix = np.arange(data_points).reshape(rows, columns)

s = time.time()

res = np.mean(matrix, axis=1)  # axis=1 - по строкам

e = time.time()
print(e - s)  # 0.4072079658508301 c. (в го такой код выполняется за 285.690921ms)

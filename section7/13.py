import numpy as np

a = np.arange(100).reshape(-1, 10)

casted_a = a.astype('d')

print(casted_a)
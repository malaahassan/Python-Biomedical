import numpy as np

a = np.arange(100).reshape(-1, 10)

#The value stored at [9][2] is 92 

print(a[2]) #third row

print(a[:, 3]) #4th column
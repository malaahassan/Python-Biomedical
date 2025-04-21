import numpy as np

a = np.arange(100).reshape(-1, 10)

# a + 1
result_add = np.add(a, 1)
print(result_add)

# a - 1
result_sub = np.subtract(a, 1)
print(result_sub)

# a * 2
result_mul = np.multiply(a, 2)
print(result_mul)

# a / 2
result_div = np.divide(a, 2)
print(result_div)

# a ** 2
result_square = np.power(a, 2)
print(result_square)
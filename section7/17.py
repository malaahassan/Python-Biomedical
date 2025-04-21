import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# a > b
result_greater_ab = np.greater(a, b)
print(result_greater_ab)

# a < b
result_less_ab = np.less(a, b)
print(result_less_ab)

# a >= b
result_greater_equal_ab = np.greater_equal(a, b)
print(result_greater_equal_ab)
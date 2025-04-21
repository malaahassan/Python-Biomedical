import numpy as np

a = np.arange(100).reshape(-1, 10)


# a > 50
result_greater_than_50 = np.greater(a, 50)
print(result_greater_than_50)

# a < 50
result_less_than_50 = np.less(a, 50)
print(result_less_than_50)

# a >= 50
result_greater_equal_50 = np.greater_equal(a, 50)
print(result_greater_equal_50)
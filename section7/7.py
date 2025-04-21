import numpy as np

array7 = np.arange(1, 10).reshape(3, 3)

array7 = array7.reshape(4, -1)

print(array7)
import numpy as np


arr = [[0, 1, 2], [3, 4, 5]]
arr = np.array(arr, dtype=int)

new = arr.reshape(6, 1)
print(new)
print(arr.resize((3, 2)))
print(arr)
print()
print(new)

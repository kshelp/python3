import numpy as np

arr3 = np.arange(5)
print(arr3)         # [0 1 2 3 4]
print([arr3.sum(), arr3.mean()])    # [10, 2.0]
print([arr3.std(), arr3.var()])
# [1.4142135623730951, 2.0]

print([arr3.min(), arr3.max()])     # [0, 4]
print([arr3.sum(), arr3.mean()])    # [10, 2.0]

arr4 = np.arange(1, 5)
print(arr4)             # [1 2 3 4]
print(arr4.cumsum())    # [ 1  3  6 10]
print(arr4.cumprod())   # [ 1  2  6 24]

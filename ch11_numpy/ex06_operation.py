import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

print(arr1 + arr2)      # [11 22 33 44]
print(arr1 - arr2)      # [ 9 18 27 36]
print(arr2 * 2)         # [2 4 6 8]
print(arr1 * arr2)      # [ 10  40  90 160]
print(arr1 / arr2)      # [10. 10. 10. 10.]
print(arr1 / (arr2 ** 2))
# [10.          5.          3.33333333  2.5       ]
print(arr1 > 20)        # [False False  True  True]

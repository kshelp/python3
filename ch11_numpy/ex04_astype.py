import numpy as np

print(np.array(['1.5', '0.62', '2', '3.14', '3.141592']))
# ['1.5' '0.62' '2' '3.14' '3.141592']

str_a1 = np.array(['1.567', '0.123', '5.123', '9', '8'])
num_a1 = str_a1.astype(float)
print(num_a1)
# [1.567 0.123 5.123 9.    8.   ]
print(str_a1.dtype)     # <U5
print(num_a1.dtype)     # float64

str_a2 = np.array(['1', '3', '5', '7', '9'])
num_a2 = str_a2.astype(int)
print(num_a2)           # [1 3 5 7 9]
print(str_a2.dtype)     # <U1
print(num_a2.dtype)     # int32

num_f1 = np.array([10, 21, 0.549, 4.75, 5.98])
num_i1 = num_f1.astype(int)
print(num_i1)           # [10 21  0  4  5]
print(num_f1.dtype)     # float64
print(num_i1.dtype)     # int32

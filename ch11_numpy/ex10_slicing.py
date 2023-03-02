import numpy as np

b1 = np.array([0, 10, 20, 30, 40, 50])
print(b1[1:4])      # [10 20 30]
print(b1[:3])       # [ 0 10 20]
print(b1[2:])       # [20 30 40 50]

b1[2:5] = np.array([25, 35, 45])
print(b1)           # [ 0 10 25 35 45 50]

b1[3:6] = 60
print(b1)           # [ 0 10 25 60 60 60]

b2 = np.arange(10, 100, 10).reshape(3,3)
print(b2)
'''
[[10 20 30]
 [40 50 60]
 [70 80 90]]
'''

print(b2[1:3, 1:3])
'''
[[50 60]
 [80 90]]
'''

print(b2[:3, 1:])
'''
[[20 30]
 [50 60]
 [80 90]]
'''

print(b2[1][0:2])       # [40 50]

b2[0:2, 1:3] = np.array([[25, 35], [55, 65]])
print(b2)
'''
[[10 25 35]
 [40 55 65]
 [70 80 90]]
'''
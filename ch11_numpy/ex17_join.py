import pandas as pd
import numpy as np

df1 = pd.DataFrame({'Class1': [95, 92, 98, 100],
                    'Class2': [91, 93, 97, 99]})
print(df1)
'''
   Class1  Class2
0      95      91
1      92      93
2      98      97
3     100      99
'''

df4 = pd.DataFrame({'Class3': [93, 91, 95, 98]})
print(df4)
'''
   Class3
0      93
1      91
2      95
3      98
'''

print(df1.join(df4))
'''
   Class1  Class2  Class3
0      95      91      93
1      92      93      91
2      98      97      95
3     100      99      98
'''

index_label = ['a', 'b', 'c', 'd']
df1a = pd.DataFrame({'Class1': [95, 92, 98, 100],
                     'Class2': [91, 93, 97, 99]}, index=index_label)
df4a = pd.DataFrame({'Class3': [93, 91, 95, 98]}, index=index_label)

print(df1a.join(df4a))
'''
   Class1  Class2  Class3
a      95      91      93
b      92      93      91
c      98      97      95
d     100      99      98
'''

df5 = pd.DataFrame({'Class4': [82, 92]})
print(df5)
'''
   Class4
0      82
1      92
'''

print(df1.join(df5))
'''
   Class1  Class2  Class4
0      95      91    82.0
1      92      93    92.0
2      98      97     NaN
3     100      99     NaN
'''

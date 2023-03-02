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

df2 = pd.DataFrame({'Class1': [87, 89],
                    'Class2': [85, 90]})
print(df2)
'''
   Class1  Class2
0      87      85
1      89      90
'''

print(df1.append(df2))
'''
   Class1  Class2
0      95      91
1      92      93
2      98      97
3     100      99
0      87      85
1      89      90
'''

print(df1.append(df2, ignore_index=True))
'''
   Class1  Class2
0      95      91
1      92      93
2      98      97
3     100      99
4      87      85
5      89      90
'''

df3 = pd.DataFrame({'Class1': [96, 83]})
print(df3)
'''
   Class1
0      96
1      83
'''

print(df2.append(df3, ignore_index=True))
'''
   Class1  Class2
0      87    85.0
1      89    90.0
2      96     NaN
3      83     NaN
'''

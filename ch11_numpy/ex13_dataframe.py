import numpy as np
import pandas as pd

print(pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
'''
   0  1  2
0  1  2  3
1  4  5  6
2  7  8  9
'''

data_list = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(pd.DataFrame(data_list))
'''
    0   1   2
0  10  20  30
1  40  50  60
2  70  80  90
'''

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
index_date = pd.date_range('2019-09-01', periods=4)
columns_list = ['A', 'B', 'C']
print(pd.DataFrame(data, index=index_date, columns=columns_list))
'''
2  70  80  90
             A   B   C
2019-09-01   1   2   3
2019-09-02   4   5   6
2019-09-03   7   8   9
2019-09-04  10  11  12
'''

table_data = {'연도': [2015, 2016, 2016, 2017, 2017],
              '지사': ['한국', '한국', '미국', '한국', '미국'],
              '고객 수': [200, 250, 450, 300, 500]}
print(table_data)
'''
{'연도': [2015, 2016, 2016, 2017, 2017], '지사': ['한국', '한국', '미국', '한 
국', '미국'], '고객 수': [200, 250, 450, 300, 500]}
'''
print(pd.DataFrame(table_data))
'''
     연도  지사  고객 수
0  2015  한국   200
1  2016  한국   250
2  2016  미국   450
3  2017  한국   300
4  2017  미국   500
'''

df = pd.DataFrame(table_data, columns=['연도', '지사', '고객 수'])
print(df)
'''
     연도  지사  고객 수
0  2015  한국   200
1  2016  한국   250
2  2016  미국   450
3  2017  한국   300
4  2017  미국   500
'''

print(df.index)     # RangeIndex(start=0, stop=5, step=1)
print(df.columns)   # Index(['연도', '지사', '고객 수'], dtype='object')
print(df.values)
'''
[[2015 '한국' 200]
 [2016 '한국' 250]
 [2016 '미국' 450]
 [2017 '한국' 300]
 [2017 '미국' 500]]
'''

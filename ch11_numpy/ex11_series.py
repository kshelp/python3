import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)
'''
0    10
1    20
2    30
3    40
4    50
dtype: int64
'''

s1.index
print(s1.index)     # RangeIndex(start=0, stop=5, step=1)
print(s1.values)    # [10 20 30 40 50]

s2 = pd.Series(['a', 'b', 'c', 1, 2, 3])
print(s2)
'''
0    a
1    b
2    c
3    1
4    2
5    3
dtype: object
'''


s3 = pd.Series([np.nan, 10, 30])
print(s3)
'''
0     NaN
1    10.0
2    30.0
dtype: float64
'''

index_date = ['2018-10-07', '2018-10-08', '2018-10-09', '2018-10-10']
s4 = pd.Series([200, 195, np.nan, 205], index=index_date)
print(s4)
'''
2018-10-07    200.0
2018-10-08    195.0
2018-10-09      NaN
2018-10-10    205.0
dtype: float64
'''

s5 = pd.Series({'국어': 100, '영어': 95, '수학': 90})
print(s5)
'''
국어    100
영어     95
수학     90
dtype: int64
'''

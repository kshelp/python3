import pandas as pd

df_A_B = pd.DataFrame({'판매월': ['1월', '2월', '3월', '4월'],
                       '제품A': [100, 150, 200, 130],
                       '제품B': [90, 110, 140, 170]})
print(df_A_B)
'''
  판매월  제품A  제품B
0  1월  100   90
1  2월  150  110
2  3월  200  140
3  4월  130  170
'''

df_C_D = pd.DataFrame({'판매월': ['1월', '2월', '3월', '4월'],
                       '제품C': [112, 141, 203, 134],
                       '제품D': [90, 110, 140, 170]})
print(df_C_D)
'''
  판매월  제품C  제품D
0  1월  112   90
1  2월  141  110
2  3월  203  140
3  4월  134  170
'''

print(df_A_B.merge(df_C_D))
'''
  판매월  제품A  제품B  제품C  제품D
0  1월  100   90  112   90
1  2월  150  110  141  110
2  3월  200  140  203  140
3  4월  130  170  134  170
'''

df_left = pd.DataFrame({'key': ['A', 'B', 'C'], 'left': [1, 2, 3]})
print(df_left)
'''
  key  left
0   A     1
1   B     2
2   C     3
'''

df_right = pd.DataFrame({'key': ['A', 'B', 'D'], 'right': [4, 5, 6]})
print(df_right)
'''
  key  right
0   A      4
1   B      5
2   D      6
'''

print(df_left.merge(df_right, how='left', on='key'))
'''
 key  left  right
0   A     1    4.0
1   B     2    5.0
2   C     3    NaN
'''

print(df_left.merge(df_right, how='right', on='key'))
'''
  key  left  right
0   A   1.0      4
1   B   2.0      5
2   D   NaN      6
'''

print(df_left.merge(df_right, how='outer', on='key'))
'''
  key  left  right
0   A   1.0    4.0
1   B   2.0    5.0
2   C   3.0    NaN
3   D   NaN    6.0
'''

print(df_left.merge(df_right, how='inner', on='key'))
'''
  key  left  right
0   A     1      4
1   B     2      5
'''

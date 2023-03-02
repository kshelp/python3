import pandas as pd

data_file = "./ch19_project/total_sales_data.csv"

df_sales = pd.read_csv(data_file)
print(df_sales)
'''
  매장명  제품종류 모델명  판매  재고
0   A  스마트폰  S1   1   2
1   A  스마트폰  S2   2   5
2   A    TV  V1   3   5
3   B  스마트폰  S2   4   6
4   B  스마트폰  S1   5   8
5   B    TV  V1   6   9
6   C  스마트폰  S2   2   4
7   C    TV  V1   3   6
8   C    TV  V2   7   9
'''

print(df_sales.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   매장명     9 non-null      object
 1   제품종류    9 non-null      object
 2   모델명     9 non-null      object
 3   판매      9 non-null      int64
 4   재고      9 non-null      int64
dtypes: int64(2), object(3)
memory usage: 488.0+ bytes
None
'''

print(df_sales['매장명'].value_counts())
'''
C    3
B    3
A    3
Name: 매장명, dtype: int64
'''

print(df_sales['제품종류'].value_counts())
'''
스마트폰    5
TV      4
Name: 제품종류, dtype: int64
'''


print(df_sales.pivot_table(index=["매장명", "제품종류", "모델명"],
                     values =["판매","재고"], aggfunc='sum'))
'''
              재고  판매
매장명 제품종류 모델명
A   TV   V1    5   3
    스마트폰 S1    2   1
         S2    5   2
B   TV   V1    9   6
    스마트폰 S1    8   5
         S2    6   4
C   TV   V1    6   3
         V2    9   7
    스마트폰 S2    4   2
'''

print(df_sales.pivot_table(index=["매장명"], columns = ["제품종류"],
                     values =["판매","재고"], aggfunc='sum'))
'''
      재고       판매
제품종류  TV 스마트폰  TV 스마트폰
매장명
A      5    7   3    3
B      9   14   6    9
C     15    4  10    2
'''

print(df_sales.pivot_table(index=["매장명"], columns = ["제품종류"],
                     values =["판매","재고"], aggfunc='count'))
'''
     재고      판매     
제품종류 TV 스마트폰 TV 스마트폰
매장명
A     1    2  1    2
B     1    2  1    2
C     2    1  2    1
'''
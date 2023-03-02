import pandas as pd

df_WH = pd.DataFrame({'Weight': [62, 67, 55, 74],
                      'Height': [165, 177, 160, 180]},
                     index=['ID_1', 'ID_2', 'ID_3', 'ID_4'])
df_WH.index.name = 'User'
print(df_WH)
'''
      Weight  Height
User
ID_1      62     165
ID_2      67     177
ID_3      55     160
ID_4      74     180
'''

bmi = df_WH['Weight']/(df_WH['Height']/100)**2
print(bmi)
'''
User
ID_1    22.773186
ID_2    21.385936
ID_3    21.484375
ID_4    22.839506
dtype: float64
'''

df_WH['BMI'] = bmi
print(df_WH)
'''
      Weight  Height        BMI
User
ID_1      62     165  22.773186
ID_2      67     177  21.385936
ID_3      55     160  21.484375
ID_4      74     180  22.839506
'''

df_WH.to_csv('D:\dev\workspace\python\ch14_numpy\save_DataFrame.csv')

df_pr = pd.DataFrame({'판매가격': [2000, 3000, 5000, 10000],
                      '판매량': [32, 53, 40, 25]},
                     index=['P1001', 'P1002', 'P1003', 'P1004'])
df_pr.index.name = '제품번호'
print(df_pr)
'''
        판매가격  판매량
제품번호
P1001   2000   32
P1002   3000   53
P1003   5000   40
P1004  10000   25
'''

file_name = 'D:\dev\workspace\python\ch14_numpy\save_DataFrame_utf-8.txt'
df_pr.to_csv(file_name, sep=" ", encoding="utf-8")

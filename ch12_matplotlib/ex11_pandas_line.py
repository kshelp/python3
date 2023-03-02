import pandas as pd
import matplotlib.pyplot as plt

s1 = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(s1)
'''
0     1
1     2
2     3
3     4
4     5
5     6
6     7
7     8
8     9
9    10
dtype: int64
'''
s1.plot()
plt.show()


s2 = pd.Series([1,2,3,4,5,6,7,8,9,10], index = pd.date_range('2019-01-01', periods=10))
print(s2)
'''
2019-01-01     1
2019-01-02     2
2019-01-03     3
2019-01-04     4
2019-01-05     5
2019-01-06     6
2019-01-07     7
2019-01-08     8
2019-01-09     9
2019-01-10    10
Freq: D, dtype: int64
'''
s2.plot()
plt.show()


s2.plot(grid=True)
plt.show()


df_rain = pd.read_csv('D:\dev\workspace\python\ch14_numpy\sea_rain1.csv', index_col="연도" )
print(df_rain)
'''
           동해       남해       서해       전체
연도
1996  17.4629  17.2288  14.4360  15.9067
1997  17.4116  17.4092  14.8248  16.1526
1998  17.5944  18.0110  15.2512  16.6044
1999  18.1495  18.3175  14.8979  16.6284
2000  17.9288  18.1766  15.0504  16.6178
'''


import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'# '맑은 고딕'으로 설정 
matplotlib.rcParams['axes.unicode_minus'] = False

df_rain.plot()
plt.show()


rain_plot = df_rain.plot(grid = True, style = ['r--*', 'g-o', 'b:*', 'm-.p'])
rain_plot.set_xlabel("연도")
rain_plot.set_ylabel("강수량")
rain_plot.set_title("연간 강수량")
plt.show()


year = [2006, 2008, 2010, 2012, 2014, 2016] # 연도
area = [26.2, 27.8, 28.5, 31.7, 33.5, 33.2] # 1인당 주거면적
table = {'연도':year, '주거면적':area}
df_area = pd.DataFrame(table, columns=['연도', '주거면적'])
print(df_area)
'''
     연도  주거면적
0  2006  26.2
1  2008  27.8
2  2010  28.5
3  2012  31.7
4  2014  33.5
5  2016  33.2
'''

df_area.plot(x='연도', y='주거면적', grid = True, title = '연도별 1인당 주거면적')
plt.show()

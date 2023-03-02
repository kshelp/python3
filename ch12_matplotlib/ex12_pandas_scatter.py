import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'   # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

temperature = [25.2, 27.4, 22.9, 26.2, 29.5, 33.1, 30.4, 36.1, 34.4, 29.1]
Ice_cream_sales = [236500, 357500, 203500, 365200,
                   446600, 574200, 453200, 675400, 598400, 463100]

dict_data = {'기온': temperature, '아이스크림 판매량': Ice_cream_sales}
df_ice_cream = pd.DataFrame(dict_data, columns=['기온', '아이스크림 판매량'])

print(df_ice_cream)
'''
     기온  아이스크림 판매량
0  25.2     236500
1  27.4     357500
2  22.9     203500
3  26.2     365200
4  29.5     446600
5  33.1     574200
6  30.4     453200
7  36.1     675400
8  34.4     598400
9  29.1     463100
'''

df_ice_cream.plot.scatter(x='기온', y='아이스크림 판매량',
                          grid=True, title='최고 기온과 아이스크림 판매량')
plt.show()

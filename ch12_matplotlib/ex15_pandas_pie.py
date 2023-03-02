import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'   # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7, 6, 3, 2, 2]

df_fruit = pd.Series(result, index=fruit, name='선택한 학생수')
print(df_fruit)
'''
사과     7
바나나    6
딸기     3
오렌지    2
포도     2
Name: 선택한 학생수, dtype: int64
'''

df_fruit.plot.pie()
plt.show()


explode_value = (0.1, 0, 0, 0, 0)
fruit_pie = df_fruit.plot.pie(figsize=(5, 5), autopct='%.1f%%', startangle=90,
                              counterclock=False, explode=explode_value, shadow=True, table=True)
fruit_pie.set_ylabel("")  # 불필요한 y축 라벨 제거
fruit_pie.set_title("과일 선호도 조사 결과")

# 그래프를 이미지 파일로 저장. dpi는 200으로 설정
plt.savefig('d:\dev\workspace\python\ch15_matplotlib\saveFigTest3.png', dpi=200)
plt.show()

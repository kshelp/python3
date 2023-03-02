import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.family'] = 'Malgun Gothic'   # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

mpl.rcParams['figure.figsize']
mpl.rcParams['figure.dpi']


x = np.arange(0, 5, 1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3

plt.plot(x, y1, x, y2, x, y3, x, y4)

plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Saving a figure')

# 그래프를 이미지 파일로 저장. dpi는 100으로 설정
plt.savefig('d:\dev\workspace\python\ch15_matplotlib\saveFigTest1.png', dpi=100)
plt.show()


fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7, 6, 3, 2, 2]
explode_value = (0.1, 0, 0, 0, 0)

plt.figure(figsize=(5, 5))  # 그래프의 크기를 지정
plt.pie(result, labels=fruit, autopct='%.1f%%', startangle=90,
        counterclock=False, explode=explode_value, shadow=True)

# 그래프를 이미지 파일로 저장. dpi는 200으로 설정
plt.savefig('d:\dev\workspace\python\ch15_matplotlib\saveFigTest2.png', dpi=200)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

height = [165, 177, 160, 180, 185, 155, 172]   # 키 데이터
weight = [62, 67, 55, 74, 90, 43, 64]   # 몸무게 데이터

plt.scatter(height, weight)
plt.xlabel('Height(m)')
plt.ylabel('Weight(Kg)')
plt.title('Height & Weight')
plt.grid(True)
plt.scatter(height, weight, s=500, c='r')  # 마커 크기는 500, 컬러는 붉은색(red)
plt.show()


size = 100 * np.arange(1, 8)  # 데이터별로 마커의 크기 지정
colors = ['r', 'g', 'b', 'c', 'm', 'k', 'y']  # 데이터별로 마커의 컬러 지정

plt.scatter(height, weight, s=size, c=colors)
plt.show()


import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'   # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

city = ['서울', '인천', '대전', '대구', '울산', '부산', '광주']

# 위도(latitude)와 경도(longitude)
lat  = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16] 
lon = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85]

# 인구 밀도(명/km^2): 2017년 통계청 자료
pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995]

size = np.array(pop_den) * 0.2 # 마커의 크기 지정 
colors = ['r', 'g', 'b', 'c', 'm', 'k', 'y'] # 마커의 컬러 지정

plt.scatter(lon, lat, s=size, c=colors, alpha=0.5)
plt.xlabel('경도(longitude)')
plt.ylabel('위도(latitude)')
plt.title('지역별 인구 밀도(2017)')

for x, y, name in zip(lon, lat, city):
    plt.text(x, y, name) # 위도 경도에 맞게 도시 이름 출력

plt.show()

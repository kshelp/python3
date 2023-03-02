import matplotlib
import numpy as np
import matplotlib.pyplot as plt
member_IDs = ['m_01', 'm_02', 'm_03', 'm_04']  # 회원 ID
before_ex = [27, 35, 40, 33]  # 운동 시작 전
after_ex = [30, 38, 42, 37]  # 운동 한 달 후


n_data = len(member_IDs)     # 회원이 네 명이므로 전체 데이터 수는 4
index = np.arange(n_data)   # NumPy를 이용해 배열 생성 (0, 1, 2, 3)
plt.bar(index, before_ex)   # bar(x,y)에서 x=index, height=before_ex 로 지정
plt.show()


plt.bar(index, before_ex, tick_label=member_IDs)
plt.show()


colors = ['r', 'g', 'b', 'm']
plt.bar(index, before_ex, color=colors, tick_label=member_IDs)
plt.show()


plt.bar(index, before_ex, tick_label=member_IDs, width=0.6)
plt.show()


colors = ['r', 'g', 'b', 'm']
plt.barh(index, before_ex, color=colors, tick_label=member_IDs)
plt.show()


matplotlib.rcParams['font.family'] = 'Malgun Gothic'   # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

barWidth = 0.4
plt.bar(index, before_ex, color='c', align='edge',
        width=barWidth, label='before')
plt.bar(index + barWidth, after_ex, color='m',
        align='edge', width=barWidth, label='after')

plt.xticks(index + barWidth, member_IDs)
plt.legend()
plt.xlabel('회원 ID')
plt.ylabel('윗몸일으키기 횟수')
plt.title('운동 시작 전과 후의 근지구력(복근) 변화 비교')
plt.show()

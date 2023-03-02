import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4.5, 5, 0.5)
y1 = 2*x**2
y2 = 5*x + 30
y3 = 4*x**2 + 10


plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()

plt.plot(x, y1, x, y2, x, y3)
plt.show()

plt.plot(x, y1)  # 처음 그리기 함수를 수행하면 그래프 창이 자동으로 생성됨
plt.figure()  # 새로운 그래프 창을 생성함

plt.plot(x, y2)  # 새롭게 생성된 그래프 창에 그래프를 그림
plt.show()


# 데이터 생성
x = np.arange(-5, 5, 0.1)
y1 = x**2 - 2
y2 = 20*np.cos(x)**2  # NumPy에서 cos()는 np.cos()으로 입력

plt.figure(1)  # 1번 그래프 창을 생성함
plt.plot(x, y1)  # 지정된 그래프 창에 그래프를 그림

plt.figure(2)  # 2번 그래프 창을 생성함
plt.plot(x, y2)  # 지정된 그래프 창에 그래프를 그림

plt.figure(1)  # 이미 생성된 1번 그래프 창을 지정함
plt.plot(x, y2)  # 지정된 그래프 창에 그래프를 그림

plt.figure(2)  # 이미 생성된 2번 그래프 창을 지정함
plt.clf()  # 2번 그래프 창에 그려진 모든 그래프를 지움
plt.plot(x, y1)  # 지정된 그래프 창에 그래프를 그림

plt.show()


# 데이터 생성
x = np.arange(0, 10, 0.1)
y1 = 0.3*(x-5)**2 + 1
y2 = -1.5*x + 3
y3 = np.sin(x)**2  # NumPy에서 sin()은 np.sin()으로 입력
y4 = 10*np.exp(-x) + 1  # NumPy에서 exp()는 np.exp()로 입력

# 2 × 2 행렬로 이뤄진 하위 그래프에서 p에 따라 위치를 지정
plt.subplot(2, 2, 1)  # p는 1
plt.plot(x, y1)

plt.subplot(2, 2, 2)  # p는 2
plt.plot(x, y2)

plt.subplot(2, 2, 3)  # p는 3
plt.plot(x, y3)

plt.subplot(2, 2, 4)  # p는 4
plt.plot(x, y4)

plt.show()

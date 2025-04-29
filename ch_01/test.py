import matplotlib.pyplot as plt
import numpy as np

# 데이터 준비
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# # 그래프 그리기
# plt.plot(x, y, label='y = 2x')  # 선 그래프
# plt.xlabel('X-axis')  # x축 라벨
# plt.ylabel('Y-axis')  # y축 라벨
# plt.title('Simple Line Plot')  # 그래프 제목
# plt.legend()  # 범례 표시
# plt.grid(True)  # 격자 표시

# # 그래프 출력
# plt.show()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(110, 4))  # 1행 2열

ax1.plot(x, y)
ax1.set_title('Plot 1')

ax2.scatter(x, y)
ax2.set_title('Plot 2')

plt.tight_layout()
plt.show()
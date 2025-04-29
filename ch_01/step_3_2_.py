from pathlib import Path
import matplotlib.pyplot as plt
from step_2_1 import OUT_DIR
from step_3_1 import load_plot_data

# 데이터 로드 (임시 데이터 사용)
# plot_data = {
#     "x": ["A", "B", "C"],
#     "y": [10, 20, 30]
# }

# 디버깅용 출력
print("Loaded plot data:", plot_data)
print("Data type:", type(plot_data))

# 그래프 생성
fig, ax = plt.subplots(figsize=(10, 6))  # 그래프 크기 조정

# 데이터 키 확인 후 수정
ax.barh(plot_data["x"], plot_data["y"], color='skyblue')  # 키 이름 수정

# 그래프 제목 및 레이블 추가
ax.set_title("Stem vs Size", fontsize=16)
ax.set_xlabel("Size", fontsize=12)
ax.set_ylabel("Stem", fontsize=12)

# 레이블 가독성을 위해 y축 정렬 조정
ax.tick_params(axis='y', labelsize=10)

# 그래프 저장
output_path = OUT_DIR / f"{Path(__file__).stem}.png"
fig.tight_layout()  # 레이아웃 조정
fig.savefig(output_path)

# 디버깅용 출력
print(f"그래프가 저장되었습니다: {output_path}")

import json
from pathlib import Path

from step_2_1 import OUT_DIR
from step_2_4 import load_filesize_per_dir

OUT_3_1 = OUT_DIR / f"{Path(__file__).stem}.json"

def dump_plot_data():
    size_per_path = load_filesize_per_dir()
    size_per_stem = {Path(path).stem: size for path,
                     size in size_per_path.items()
                     if size > 0}
    plot_data = dict(
        stem = list(size_per_stem.keys()),
        size = list(size_per_stem.values()),
    )

    with open(OUT_3_1, "w", encoding="utf-8") as fp:
        json.dump(plot_data, fp, ensure_ascii=False, indent=2)

# step_3_1.py 파일에서 load_plot_data 함수 수정
def load_plot_data():
    # 데이터 로드 로직
    print("load_plot_data 함수 호출됨")
    # 반환되는 데이터 확인
    data = {}  # 실제 데이터 로드 로직으로 교체
    print("로드된 데이터:", data)
    return data

if __name__ == "__main__":
    dump_plot_data()

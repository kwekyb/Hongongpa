from pathlib import Path

WORK_DIR = Path(__file__).parent
OUT_DIR = WORK_DIR / "output"
# print(f"work-dir: {WORK_DIR}")
# print(f"out-dir: {OUT_DIR}")

if __name__ == "__main__":
    OUT_DIR.mkdir(exist_ok=True)

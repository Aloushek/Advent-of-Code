from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")
OUTPUT_FILE = Path(SCRIPT_DIR, "output/output.png")


def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().split("\n\n")

    elfs = []
    for elfdata in data:
        elfs.append(sum(map(int, elfdata.splitlines())))
    print(max(elfs))  # part 1
    print(sum(sorted(elfs)[-3:]))  # part 2


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

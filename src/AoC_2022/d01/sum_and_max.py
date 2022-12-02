from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")
OUTPUT_FILE = Path(SCRIPT_DIR, "output/output.png")

def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()
        
    print(data)
    elfs = [0]
    elfIndex = 0
    for i in range(0, len(data)):
        if (data[i] == ""):
            elfIndex += 1
            elfs.append(0)
        else:
            elfs[elfIndex] += int(data[i])

    # part 1
    print(max(elfs))
    # part 2
    first = max(elfs)
    elfs.remove(first)
    second = max(elfs)
    elfs.remove(second)
    third = max(elfs)
    print(first + second + third)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")


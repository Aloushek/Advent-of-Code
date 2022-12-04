from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")
OUTPUT_FILE = Path(SCRIPT_DIR, "output/output.png")

def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()

    same = 0
    for pairstring in data:
        pair = pairstring.split(",")
        elf1 = list(map(int, pair[0].split("-")))
        elf2 = list(map(int, pair[1].split("-")))
        if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1] or
            elf1[0] <= elf2[0] and elf1[1] >= elf2[1]):
            same += 1
    print(same)
    # part 2
    same = 0
    for pairstring in data:
        pair = pairstring.split(",")
        elf1 = list(map(int, pair[0].split("-")))
        elf2 = list(map(int, pair[1].split("-")))
        if (elf1[0] >= elf2[1] and elf1[1] <= elf2[0] or
            elf1[0] <= elf2[1] and elf1[1] >= elf2[0]):
            same += 1

    print(same)

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")


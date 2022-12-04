from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")
OUTPUT_FILE = Path(SCRIPT_DIR, "output/output.png")

def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()

    def getprio(common):
        priority = ord(common_characters) % 96
        if (priority > 26):
            return priority - 38
        else:
            return priority

    commonletters = []
    s = 0
    for compartment in data:
        part1 = compartment[:len(compartment)//2]
        part2 = compartment[len(compartment)//2:]
        common_characters = ''.join(
            set(part1).intersection(part2)
        )
        s += getprio(common_characters)
    print(s)

    #part2
    s = 0
    subList = [data[n:n + 3] for n in range(0, len(data), 3)]
    print(subList)

    for group in subList:
        common_characters = ''.join(
            set(group[0]).intersection(group[1]).intersection(group[2])
        )
        s += getprio(common_characters)
    print(s)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")


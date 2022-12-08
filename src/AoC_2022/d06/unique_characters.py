from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")
OUTPUT_FILE = Path(SCRIPT_DIR, "output/output.png")

def main():
    with open(INPUT_FILE, mode="rt") as f:
        input_hash = f.read()

    def characters_unique(string):
        return len(string) == len(''.join(set(string)))
    def find_unique_count(count):
        i = 0
        while(i < len(input_hash) - count):
            if (characters_unique(input_hash[i:i+count])):
                return i + count
            i += 1

    # part 1
    print(find_unique_count(4))
    # part 2
    print(find_unique_count(14))

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")


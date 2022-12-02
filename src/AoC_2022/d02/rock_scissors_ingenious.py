from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")
OUTPUT_FILE = Path(SCRIPT_DIR, "output/output.png")

def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()

    myscore = 0
    # A - rock , B - paper, C - scissors
    # X - rock 1, Y - paper 2, Z - scissors 3

    possibilities = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    #part 1
    for match in data:
        myscore += possibilities[match]
        
    print(myscore)
    #part 2 - y draw, x lose, z win

    possibilities2 = {
        "A X": "A Z",
        "A Y": "A X",
        "A Z": "A Y",
        "B X": "B X",
        "B Y": "B Y",
        "B Z": "B Z",
        "C X": "C Y",
        "C Y": "C Z",
        "C Z": "C X",
    }
    myscore2 = 0
    for match in data:
        myscore2 += possibilities[possibilities2[match]]

    print(myscore2)

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")


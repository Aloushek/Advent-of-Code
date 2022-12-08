from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")
OUTPUT_FILE = Path(SCRIPT_DIR, "output/output.png")

def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().split("\n\n")

    # part 1
    # prepare fking data
    stacks = data[0].splitlines()
    moves = data[1].splitlines()

    column_stacks = []
    column_numbers = list(map(int, stacks.pop().split("   ")))
    for column in column_numbers:
        column_stacks.append([])

    stack_index = 0
    for stack in stacks:
        for letter in stack.split("    "):
            column_stacks[stack_index].extend(letter.split(" "))
        stack_index += 1

    print(column_stacks.pop())

    rotated_stack = list(zip(*column_stacks[::-1]))

    final_stacks = []
    final_stacks2 = []
    for f in rotated_stack:
        final_stacks.append([i for i in list(f) if i])
        final_stacks2.append([i for i in list(f) if i])


    def parse_move(move):
        [items_count, places] = move.split(" from ")
        items_count = items_count.split("move ")[1]
        places = places.split(" to ")
        return [items_count, places]
    # process data

    for move in moves:
        [items_count, places] = parse_move(move)
        for _ in range(int(items_count)):
            final_stacks[int(places[1]) - 1].append(final_stacks[int(places[0]) - 1].pop())
    result1 = []
    for final_stack in final_stacks:
        result1.append(final_stack.pop())

    print("".join(list(map(lambda l: l[1], result1))))

    # part 2

    for move in moves:
        [items_count, places] = parse_move(move)
        to_move = final_stacks2[int(places[0]) - 1][-int(items_count):]
        del final_stacks2[int(places[0]) - 1][-int(items_count):]
        final_stacks2[int(places[1]) - 1].extend(to_move)

    result2 = []
    for final_stack in final_stacks2:
        result2.append(final_stack.pop())

    print("".join(list(map(lambda l: l[1], result2))))



if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")


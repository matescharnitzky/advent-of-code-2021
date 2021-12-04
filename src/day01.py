
# imports

from typing import List

# raw inputs
raw = """199
200
208
210
200
207
240
269
260
263"""

# split raw inputs into a list
examples = [int(x) for x in raw.split('\n')]

# task 1 and 2
def count_increases(inputs: List[int], window: int = 1) -> int:

    """
    Count the number of increases in a list.
    """

    count = 0
    for i in range(len(inputs) - window):

        if inputs[i + window] > inputs[i]:
            count += 1

    return count

assert count_increases(examples, 1) == 7
assert count_increases(examples, 3) == 5

if __name__ == "__main__":
    with open("./data/day01.txt") as f:
        raw = f.read()
    inputs = [int(x) for x in raw.split('\n')]
    print("Task #1 solution: {}".format(count_increases(inputs, 1)))
    print("Task #2 solution: {}".format(count_increases(inputs, 3)))
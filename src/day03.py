
from collections import Counter
from typing import List

# raw
raw = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

# examples
examples = raw.splitlines()


# task 1
def calc_consumption(numbers: List[str]) -> int:
    
    m = len(numbers[0])
    counts = [
        Counter(number[i] for number in numbers)
        for i in range(m)
    ]
    
    # gamma rate
    gamma = "".join(
        counter.most_common(1)[0][0]
        for counter in counts
    )

    # epsilon rate
    epsilon = "".join(["1" if x == "0" else "0" for x in gamma])
    
    return int(gamma, 2) * int(epsilon, 2)


assert calc_consumption(examples) == 198

if __name__ == "__main__":
    with open("./data/day03.txt") as f:
        raw = f.read()
    reports = [x for x in raw.splitlines()]
    print("Task #1 solution: {}".format(calc_consumption(reports)))

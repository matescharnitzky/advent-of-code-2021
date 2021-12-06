
from statistics import mode
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

# reports
examples = [x for x in raw.splitlines()]

# task 1
def calc_consumption(reports: List[str]) -> int:

    # find most common bits
    common_bits = []
    
    for i in range(len(reports[0])):
        common_bits.append(mode([report[i] for report in reports]))

    # gamma rate
    gamma = "".join(common_bits)

    # epsilon rate
    epsilon = "".join(["1" if x == "0" else "0" for x in gamma])
    
    return int(gamma, 2) * int(epsilon, 2)

assert calc_consumption(examples) == 198

# task 2
    
if __name__ == "__main__":
    with open("./data/day03.txt") as f:
        raw = f.read()
    reports = [x for x in raw.splitlines()]
    print("Task #1 solution: {}".format(calc_consumption(reports)))

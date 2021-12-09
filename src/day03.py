
from collections import Counter
from typing import List
import re

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


# task 2
def calc_oxygen_rate(numbers: List[str]) -> str:

    # length of bits
    m = len(numbers[0])

    # oxygen rate
    pattern = ""

    # start from complete list
    subset = numbers

    for i in range(m):

        # count bits
        counter = Counter(number[i] for number in subset)

        # find most common bit
        common_bit, common_count = counter.most_common(1)[0]

        # find least common bit
        least_bit, least_count = counter.most_common()[1]

        # update pattern
        if common_count == least_count:
            pattern += "1"
        else:
            pattern += common_bit

        # create regex
        r = re.compile(r"^" + pattern + ".*")

        # find subset
        subset = list(filter(r.match, subset))

        # break if only one left
        if len(subset) == 1:
            break

    return subset[0]


def calc_co2_rate(numbers: List[str]) -> str:

    # length of bits
    m = len(numbers[0])

    # co2 rate
    pattern = ""

    # start from complete list
    subset = numbers

    for i in range(m):

        # count bits
        counter = Counter(number[i] for number in subset)

        # find most common bit
        common_bit, common_count = counter.most_common(1)[0]

        # find least common bit
        least_bit, least_count = counter.most_common()[1]

        # update pattern
        if common_count == least_count:
            pattern += "0"
        else:
            pattern += least_bit

        # create regex
        r = re.compile(r"^" + pattern + ".*")

        # find subset
        subset = list(filter(r.match, subset))

        # break if only one left
        if len(subset) == 1:
            break

    return subset[0]


def calc_life_support(numbers: List[str]) -> int:

    # calc oxygen rate
    oxygen = calc_oxygen_rate(numbers)

    # calc co2 rate
    co2 = calc_co2_rate(numbers)

    return int(oxygen, 2) * int(co2, 2)


assert calc_oxygen_rate(examples) == "10111"
assert calc_co2_rate(examples) == "01010"
assert calc_life_support(examples) == 230

if __name__ == "__main__":
    with open("./data/day03.txt") as f:
        raw = f.read()
    reports = [x for x in raw.splitlines()]
    print("Task #1 solution: {}".format(calc_consumption(reports)))
    print("Task #2 solution: {}".format(calc_life_support(reports)))


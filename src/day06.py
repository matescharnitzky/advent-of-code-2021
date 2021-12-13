
from typing import List

RAW = "3,4,3,1,2"
AGES = [int(x) for x in RAW.split(",")]


def simulate(ages: List[int], days: int):

    for i in range(1, days+1):
        eights = [8 for age in ages if age == 0]
        ages = [6 if age == 0 else age - 1 for age in ages] + eights

    m = len(ages)

    return m


assert simulate(AGES, 18) == 26
assert simulate(AGES, 80) == 5934
assert simulate(AGES, 256) == 26984457539


if __name__ == "__main__":
    RAW = open("./data/day06.txt").read()
    AGES = [int(x) for x in RAW.split(",")]
    print("Task #1 solution: {}".format(simulate(AGES, 80)))



from typing import List, Tuple
from itertools import combinations

RAW = "16,1,2,0,4,2,7,1,2,14"
INPUT = [int(x) for x in RAW.split(",")]


def find_best_position(positions: List[int], consumption: str = "constant") -> Tuple:

    best_position = None
    least_fuel = 10000000000000000000

    for position in range(min(positions), max(positions)+1):

        fuel = 0
        for x in positions:
            if consumption == "constant":
                fuel += abs(position - x)
            elif consumption == "incremental":
                fuel += sum(range(1, abs(position - x) + 1))

        if fuel < least_fuel:
            least_fuel = fuel
            best_position = position

    return best_position, least_fuel


p, f = find_best_position(INPUT, "constant")
assert p == 2
assert f == 37
p, f = find_best_position(INPUT, "incremental")
assert p == 5
assert f == 168

if __name__ == "__main__":
    RAW = open("./data/day07.txt").read()
    INPUT = [int(x) for x in RAW.split(",")]
    p, v = find_best_position(INPUT, "constant")
    print("Task #1 solution: {}".format(v))
    p, v = find_best_position(INPUT, "incremental")
    print("Task #2 solution: {}".format(v))



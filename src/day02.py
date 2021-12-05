
from typing import List

# inputs

raw = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

# split raw inputs into a list
commands = [line.split()[0] for line in raw.split('\n')]
steps = [int(line.split()[1]) for line in raw.split('\n')]

# taks 1
def calc_product1(commands: List[str], steps: List[int]) -> int:

    horizontal = 0
    depth = 0

    for i, v in enumerate(commands):

        if v == "forward":
            horizontal += steps[i]
        
        if v == "down":
            depth += steps[i]
        
        if v == "up":
            depth -= steps[i]
    
    return horizontal * depth

assert calc_product1(commands, steps) == 150

# task 2
def calc_product2(commands: List[str], steps: List[int]) -> int:
    
    horizontal = 0
    depth = 0
    aim = 0

    for i, v in enumerate(commands):

        if v == "forward":
            horizontal += steps[i]
            depth += steps[i] * aim
        
        if v == "down":
            aim += steps[i]
        
        if v == "up":
            aim -= steps[i]
    
    return horizontal * depth

assert calc_product2(commands, steps) == 900


if __name__ == "__main__":
    with open("./data/day02.txt") as f:
        raw = f.read()
    commands = [line.split()[0] for line in raw.split('\n')]
    steps = [int(line.split()[1]) for line in raw.split('\n')]
    print("Task #1 solution: {}".format(calc_product1(commands, steps)))
    print("Task #2 solution: {}".format(calc_product2(commands, steps)))
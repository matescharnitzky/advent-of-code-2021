
from typing import List

RAW = "3,4,3,1,2"
TIMERS = [int(x) for x in RAW.split(",")]


class LanternFish:

    def __init__(self, timers: List[int]) -> None:
        self.timers = [0 for _ in range(9)]

        for timer in timers:
            self.timers[timer] += 1

    def step(self) -> None:
        new_timers = self.timers[1:] + [0]
        new_timers[8] += self.timers[0]
        new_timers[6] += self.timers[0]
        self.timers = new_timers

    def count(self) -> int:
        return sum(self.timers)


lf = LanternFish(TIMERS)
for _ in range(18):
    lf.step()
assert lf.count() == 26

lf = LanternFish(TIMERS)
for _ in range(80):
    lf.step()
assert lf.count() == 5934

lf = LanternFish(TIMERS)
for _ in range(256):
    lf.step()
assert lf.count() == 26984457539


if __name__ == "__main__":
    RAW = open("./data/day06.txt").read()
    TIMERS = [int(x) for x in RAW.split(",")]
    lf = LanternFish(TIMERS)
    for _ in range(80):
        lf.step()
    print("Task #1 solution: {}".format(lf.count()))
    lf = LanternFish(TIMERS)
    for _ in range(256):
        lf.step()
    print("Task #2 solution: {}".format(lf.count()))


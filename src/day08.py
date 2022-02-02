
from typing import List

from dataclasses import dataclass

RAW = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


@dataclass
class Display:
    input: List[str]
    output: List[str]

    @staticmethod
    def parse(line):
        input, output = [x.split() for x in line.split(" | ")]
        return Display(input, output)


displays = [Display.parse(line) for line in RAW.splitlines()]


def count_unique_segments(d):

    count = [
        1 for display in d
        for pattern in display.output
        if len(pattern) in [2, 3, 4, 7]
    ]

    return sum(count)


assert count_unique_segments(displays) == 26


def _is_one(s):
    if len(s) == 2:
        return True


def _is_four(s):
    if len(s) == 4:
        return True


def _is_seven(s):
    if len(s) == 3:
        return True


def _is_eight(s):
    if len(s) == 7:
        return True


class Decoder:
    def __init__(self, inputs: List[str]):
        self.inputs = inputs
        self.zero = None
        self.one = None
        self.two = None
        self.three = None
        self.four = None
        self.five = None
        self.six = None
        self.seven = None
        self.eight = None
        self.nine = None

    def fit(self):

        for input in self.inputs:
            if _is_one(input):
                self.one = input
            elif _is_four(input):
                self.four = input
            elif _is_seven(input):
                self.seven = input
            elif _is_eight(input):
                self.eight = input


decoder = Decoder(displays[0].input)
decoder.fit()
print(decoder.one)
print(decoder.four)
print(decoder.seven)
print(decoder.eight)


if __name__ == "__main__":
    RAW = open("./data/day08.txt").read()
    displays = [Display.parse(line) for line in RAW.splitlines()]
    print("Task #1 solution: {}".format(count_unique_segments(displays)))

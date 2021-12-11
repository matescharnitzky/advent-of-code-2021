
from typing import List, Tuple
import numpy as np

# raw
raw = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


# parse data
def parse_data(s: str) -> Tuple[List, List, List]:

    # lines
    lines = [line for line in s.splitlines() if line != ""]
    m = len(lines)

    # numbers
    numbers = [int(x) for x in lines[0].split(",")]

    # boards
    data = [list(map(int, x.split())) for x in lines[1:]]
    n_boards = int((m-1)/5)
    boards = []
    for i in range(n_boards):
        boards.append(np.array(data[(i*5):((i+1)*5)]))

    # indicators
    indicators = [np.zeros((5, 5), np.int8) for i in range(n_boards)]

    return numbers, boards, indicators


numbers, boards, indicators = parse_data(raw)


def calc_winning_score(numbers: List[int],
                       boards: List[np.ndarray],
                       indicators: List[np.ndarray]) -> int:

    for number in numbers:
        for i, board in enumerate(boards):
            indicators[i][board == number] = 1

            col_bingo = np.sum(indicators[i], 0) == 5
            row_bingo = np.sum(indicators[i], 1) == 5

            if np.sum(col_bingo) > 0:
                return number * np.sum(board[indicators[i] != 1])
            if np.sum(row_bingo) > 0:
                return number * np.sum(board[indicators[i] != 1])


assert calc_winning_score(numbers, boards, indicators) == 4512

if __name__ == "__main__":
    raw = open("./data/day04.txt").read()
    numbers, boards, indicators = parse_data(raw)
    print("Task #1 solution: {}".format(calc_winning_score(numbers, boards, indicators)))
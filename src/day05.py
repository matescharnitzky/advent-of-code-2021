
from typing import List
from dataclasses import dataclass


RAW = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


@dataclass
class Coordinate:
    x1: int
    y1: int
    x2: int
    y2: int

    @staticmethod
    def parse_coordinates(s):
        p1, p2 = s.split(" -> ")
        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")
        return Coordinate(int(x1), int(y1), int(x2), int(y2))


COORDINATES = [Coordinate.parse_coordinates(s) for s in RAW.splitlines()]


@dataclass
class Point:
    x: int
    y: int

    @staticmethod
    def find_hv_lines(coordinate):

        if coordinate.x1 == coordinate.x2:
            return [Point(coordinate.x1, y) for y in range(min(coordinate.y1, coordinate.y2), max(coordinate.y1, coordinate.y2) + 1)]

        if coordinate.y1 == coordinate.y2:
            return [Point(x, coordinate.y1) for x in range(min(coordinate.x1, coordinate.x2), max(coordinate.x1, coordinate.x2) + 1)]

    @staticmethod
    def find_hvd_lines(coordinate):

        if coordinate.x1 == coordinate.x2:
            return [Point(coordinate.x1, y) for y in range(min(coordinate.y1, coordinate.y2), max(coordinate.y1, coordinate.y2) + 1)]

        if coordinate.y1 == coordinate.y2:
            return [Point(x, coordinate.y1) for x in range(min(coordinate.x1, coordinate.x2), max(coordinate.x1, coordinate.x2) + 1)]

        if abs(coordinate.x1 - coordinate.x2) == abs(coordinate.y1 - coordinate.y2):

            d = abs(coordinate.x1 - coordinate.x2)

            if coordinate.x2 > coordinate.x1:
                xs = [x for x in range(coordinate.x1, coordinate.x2 + 1)]
            else:
                xs = [x for x in range(coordinate.x1, coordinate.x2 - 1, -1)]

            if coordinate.y2 > coordinate.y1:
                ys = [y for y in range(coordinate.y1, coordinate.y2 + 1)]
            else:
                ys = [y for y in range(coordinate.y1, coordinate.y2 - 1, -1)]

            return [Point(x, y) for x, y in zip(xs, ys)]


HV_LINES = [Point.find_hv_lines(coordinate) for coordinate in COORDINATES]
HVD_LINES = [Point.find_hvd_lines(coordinate) for coordinate in COORDINATES]


@dataclass
class Diagram:
    table: List[List[int]]

    @staticmethod
    def init_table(coordinates, lines):

        xmax = 0
        ymax = 0

        for coordinate in coordinates:
            xmax = max(xmax, coordinate.x1, coordinate.x2)
            ymax = max(ymax, coordinate.y1, coordinate.y2)

        table = []
        for _ in range(xmax+1):
            table.append([0 for _ in range(ymax+1)])

        for line in lines:
            if line is not None:
                for point in line:
                    table[point.x][point.y] += 1

        return Diagram(table)

    def count_nb_dangerous(self):

        nb_dangerous = 0

        for col in self.table:
            for element in col:
                if element >= 2:
                    nb_dangerous += 1

        return nb_dangerous


DIAGRAM = Diagram.init_table(COORDINATES, HV_LINES)
assert DIAGRAM.count_nb_dangerous() == 5

DIAGRAM = Diagram.init_table(COORDINATES, HVD_LINES)
assert DIAGRAM.count_nb_dangerous() == 12

if __name__ == "__main__":
    RAW = open("./data/day05.txt").read()
    COORDINATES = [Coordinate.parse_coordinates(s) for s in RAW.splitlines()]
    HV_LINES = [Point.find_hv_lines(coordinate) for coordinate in COORDINATES]
    HVD_LINES = [Point.find_hvd_lines(coordinate) for coordinate in COORDINATES]
    DIAGRAM = Diagram.init_table(COORDINATES, HV_LINES)
    print("Task #1 solution: {}".format(DIAGRAM.count_nb_dangerous()))
    DIAGRAM = Diagram.init_table(COORDINATES, HVD_LINES)
    print("Task #2 solution: {}".format(DIAGRAM.count_nb_dangerous()))


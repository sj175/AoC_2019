from typing import Callable, Dict, List, Set, Tuple


# 12302 is too low

def read_input() -> str:
    with open('day3.txt', 'r') as f:
        return f.read()


def man_dist(x: Tuple[int, int]) -> int:
    return abs(x[0]) + abs(x[1])


def part_1(problem_input: str) -> int:
    directions: Dict[str, Callable[[Tuple[int, int], int], Tuple[int, int]]] = {"D": lambda x, y: (x[0], x[1] - y),
                                                                                "U": lambda x, y: (x[0], x[1] + y),
                                                                                "R": lambda x, y: (x[0] + y, x[1]),
                                                                                "L": lambda x, y: (x[0] - y, x[1])}
    lines: List[str] = problem_input.split("\n")[:2]
    point_count: Dict[int, Set[Tuple[int, int]]] = {}
    my_min = 9999999999
    for i, line in enumerate(lines):
        current = (0, 0)
        points = set()
        instr = line.split(",")
        for instruction in instr:
            direction, magnitude = instruction[0], int(instruction[1:])
            for _ in range(magnitude):
                current = directions[direction](current, 1)
                points.add(current)

        point_count[i] = points

    for x in point_count[0]:
        if x in point_count[1]:
            my_min = min(man_dist(x), my_min)

    return my_min


def part_2(problem_input: str) -> int:
    directions: Dict[str, Callable[[Tuple[int, int], int], Tuple[int, int]]] = {"D": lambda x, y: (x[0], x[1] - y),
                                                                                "U": lambda x, y: (x[0], x[1] + y),
                                                                                "R": lambda x, y: (x[0] + y, x[1]),
                                                                                "L": lambda x, y: (x[0] - y, x[1])}
    lines: List[str] = problem_input.split("\n")[:2]
    point_count: Dict[int, Dict[Tuple[int, int], int]] = {}
    my_min = 9999999999
    for i, line in enumerate(lines):
        current = (0, 0)
        counter = 0
        points: Dict[Tuple[int, int], int] = {}
        instr = line.split(",")
        for instruction in instr:
            direction, magnitude = instruction[0], int(instruction[1:])
            for _ in range(magnitude):
                counter += 1
                current = directions[direction](current, 1)
                if points.get(current):
                    pass
                else:
                    points[current] = counter

        point_count[i] = points

    for x in point_count[0]:
        if x in point_count[1]:
            my_min = min(point_count[0][x] + point_count[1][x], my_min)

    return my_min


def main():
    x = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
    print(part_1(x) == 159)
    x = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
    print(part_1(x) == 135)

    print(part_1(read_input()))

    x = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""

    print(part_2(x) == 610)

    x = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""

    print(part_2(x) == 410)

    print(part_2(read_input()))


if __name__ == '__main__':
    main()

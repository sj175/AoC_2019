from typing import Callable, Dict, List, Set, Tuple


def part_1() -> int:
    start = 382345
    end = 843167
    total = 0

    for number in range(start, end + 1):
        if check_number(str(number)):
            total += 1

    return total


def check_number(problem_input: str) -> bool:
    # two adjacent digits are the same
    previous = 0
    double = False
    for current in range(1, len(problem_input)):
        if int(problem_input[current]) < int(problem_input[previous]):
            return False
        if int(problem_input[previous]) == int(problem_input[current]):
            double = True
        previous += 1

    return double


def part_2(problem_input: str) -> int:
    pass


def main():
    x = "111111"
    print(check_number(x) is True)
    x = "223450"
    print(check_number(x) is False)
    x = "123789"
    print(check_number(x) is False)

    print(part_1())


if __name__ == '__main__':
    main()

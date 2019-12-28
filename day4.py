def part_1() -> int:
    start = 382345
    end = 843167
    total = 0

    for number in range(start, end + 1):
        if check_number(str(number)):
            total += 1

    return total


def check_number(problem_input: str) -> bool:
    previous = 0
    double = False
    for current in range(1, len(problem_input)):
        if int(problem_input[current]) < int(problem_input[previous]):
            return False
        if int(problem_input[previous]) == int(problem_input[current]):
            double = True
        previous += 1

    return double


def check_number_2(problem_input: str) -> bool:
    previous = 0
    current = 1
    triple = True
    seen_a_double = False
    length = len(problem_input)
    while current < length:
        if int(problem_input[current]) < int(problem_input[previous]):
            return False
        if int(problem_input[current]) == int(problem_input[previous]):
            if previous >= 1:
                triple = int(problem_input[previous - 1]) == int(problem_input[previous])
            if current < length - 1:
                triple = int(problem_input[current + 1]) == int(problem_input[current])
                while current < length - 1 and int(problem_input[current]) == int(problem_input[current + 1]):
                    current += 1
                    previous += 1
            if not triple:
                seen_a_double = True

        previous += 1
        current += 1

    return seen_a_double


def part_2() -> int:
    start = 382345
    end = 843167
    total = 0

    for number in range(start, end + 1):
        if check_number_2(str(number)):
            total += 1

    return total


def main():
    x = "111111"
    print(check_number(x) is True)
    x = "223450"
    print(check_number(x) is False)
    x = "123789"
    print(check_number(x) is False)

    print("PART 1:", part_1())  # should be 460

    x = "112233"
    print(check_number_2(x) is True)
    x = "123444"
    print(check_number_2(x) is False)
    x = "111122"
    print(check_number_2(x) is True)
    x = "112222"
    print(check_number_2(x) is True)
    x = "1112589"
    print(check_number_2(x) is False)

    print("PART 2:", part_2())


if __name__ == '__main__':
    main()

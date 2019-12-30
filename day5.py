def get_input() -> str:
    return input(">")


def return_output(output: int) -> int:
    print(output)


def process(opcode: int, *vals, mem_location, worktape):
    if opcode == 1:
        worktape[mem_location] = worktape[vals[0]] + worktape[vals[1]]
        return True
    elif opcode == 2:
        worktape[mem_location] = worktape[vals[0]] * worktape[vals[1]]
        return True
    elif opcode == 3:
        worktape[mem_location] = get_input()
    elif opcode == 4:
        return_output(worktape[mem_location])
    elif opcode == 99:
        print("DONE")
        return False
    else:
        print("ERROR")
        raise Exception("it's fucked")


def opcode_decoder(opcode: str) -> int:
    pass


def part_1():
    run()


def run():
    program = read_file().split(",")

    current = 0
    while process(program[current], program[current + 1], program[current + 2], program[current + 3], program):
        current += 4

    return program[0]


def read_file():
    with open('day5.txt', 'r') as f:
        return f.read()


if __name__ == '__main__':
    part_1()

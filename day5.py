def process(opcode, index1, index2, output_index, program):
    if opcode == 1:
        program[output_index] = program[index1] + program[index2]
        return True
    elif opcode == 2:
        program[output_index] = program[index1] * program[index2]
        return True
    elif opcode == 99:
        print("DONE")
        print("value at position 0: ", program[0])
        return False
    else:
        print("ERROR")
        raise Exception("it's fucked")


def part_1():
    run(12, 2)


def run(noun, verb):
    p1_input = read_file()
    program = list(map(int, p1_input.split(",")))
    program[1] = noun
    program[2] = verb

    current = 0
    while process(program[current], program[current + 1], program[current + 2], program[current + 3], program):
        current += 4

    return program[0]


def read_file():
    with open('day5.txt', 'r') as f:
        return f.read()


if __name__ == '__main__':
    part_1()

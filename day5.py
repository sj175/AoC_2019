from typing import Tuple, List


# 13294380 is right, but I didn't get a 0 on the first output. this is because line 26 assumes we never have mode 1 for
# opcode 4. I should treat the "output" locations differently to parameters, then this problem will be solved.

def get_input() -> str:
    return input(">")


def return_output(output: int) -> None:
    print(output)


def process(opcode: int, *parameters: int, worktape: list):
    if opcode == 1:
        worktape[parameters[-1]] = parameters[0] + parameters[1]
        return True
    elif opcode == 2:
        worktape[parameters[-1]] = parameters[0] * parameters[1]
        return True
    elif opcode == 3:
        worktape[parameters[-1]] = get_input()
        return True
    elif opcode == 4:
        return_output(parameters[-1])
        return True
    elif opcode == 7:
        worktape[parameters[-1]] = 1 if parameters[0] < parameters[1] else 0
        return True
    elif opcode == 8:
        worktape[parameters[-1]] = 1 if parameters[0] == parameters[1] else 0
    elif opcode == 99:
        print("DONE")
        return False
    else:
        print("ERROR")
        raise Exception("it's fucked")


def fetch_parameters(opcode: int, parameter_modes: List[str], memory: List[str], *parameter_data: int) -> Tuple[
    int, ...]:
    """fetches the parameters and returns a tuple consisting of each parameter. The final element of the tuple is the
    output address for this instruction. Opcode 4 does not necessarily have an output address so it is optional"""
    opcode_length = {1: 4, 2: 4, 3: 2, 4: 2, 99: 1}  # todo: remove duplication
    num_of_params = opcode_length[opcode] - 1
    params = []

    while len(parameter_modes) < num_of_params:
        parameter_modes.append("0")

    assert len(parameter_modes) == len(parameter_data) == num_of_params

    for i, mode in enumerate(parameter_modes):
        if opcode != 4 and i == len(parameter_modes) - 1:
            params.append(int(parameter_data[i]))
            break
        if mode == '0':
            params.append(int(memory[parameter_data[i]]))
        elif mode == '1':
            params.append(parameter_data[i])
        else:
            print("unsupported parameter mode:", mode)

    assert len(params) == num_of_params

    return tuple(params)


def opcode_decoder(opcode_data: str) -> int:
    return int(opcode_data[-2] + opcode_data[-1])


def part_1():
    # run("""1002,4,3,4,33""")

    run(read_file())


def run(problem_input: str):
    program = problem_input.split(",")
    opcode_length = {1: 4, 2: 4, 3: 2, 4: 2, 99: 1}

    current = 0
    while True:
        opcode_data = str(program[current]).rjust(2, "0")
        opcode = opcode_decoder(opcode_data)
        parameter_data = program[current + 1:current + opcode_length[opcode]]
        parameters = fetch_parameters(opcode, list(opcode_data[:-2][::-1]), program, *map(int, parameter_data))
        if not process(opcode, *parameters, worktape=program):  # todo fix this
            break
        current += opcode_length[opcode]

    return program[0]


def read_file():
    with open('day5.txt', 'r') as f:
        return f.read()


if __name__ == '__main__':
    part_1()

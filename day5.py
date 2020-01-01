from typing import Tuple, List


# 13294380 is right, but I didn't get a 0 on the first output. this is because line 26 assumes we never have mode 1 for
# opcode 4. I should treat the "output" locations differently to parameters, then this problem will be solved.

def get_input() -> str:
    return input(">")


def return_output(output: int) -> None:
    print(output)


def process(opcode: int, *parameters: int, worktape: list, pc: int):
    opcode_length = opcode_length = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 99: 1}
    if opcode == 1:
        worktape[parameters[-1]] = parameters[0] + parameters[1]
    elif opcode == 2:
        worktape[parameters[-1]] = parameters[0] * parameters[1]
    elif opcode == 3:
        worktape[parameters[-1]] = get_input()
    elif opcode == 4:
        return_output(parameters[-1])
    elif opcode == 5:
        if parameters[0] != 0:
            return parameters[1]
    elif opcode == 6:
        if parameters[0] == 0:
            return parameters[1]
    elif opcode == 7:
        worktape[parameters[-1]] = 1 if parameters[0] < parameters[1] else 0
    elif opcode == 8:
        worktape[parameters[-1]] = 1 if parameters[0] == parameters[1] else 0
    elif opcode == 99:
        print("DONE")
        return -1
    else:
        print("ERROR")
        raise Exception(f"received unknown opcode: {opcode}")

    return pc + opcode_length[opcode]


def fetch_parameters(opcode: int, parameter_modes: List[str], memory: List[str], *parameter_data: int) -> Tuple[
    int, ...]:
    """fetches the parameters and returns a tuple consisting of each parameter. The final element of the tuple is the
    output address for this instruction. Opcode 4 does not necessarily have an output address so it is optional"""
    opcode_length = opcode_length = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 99: 1}  # todo: remove duplication
    num_of_params = opcode_length[opcode] - 1
    params = []

    while len(parameter_modes) < num_of_params:
        parameter_modes.append("0")

    assert len(parameter_modes) == len(parameter_data) == num_of_params

    for i, mode in enumerate(parameter_modes):
        if opcode not in {4, 5, 6} and i == len(parameter_modes) - 1:
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

    # run("""3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9""")
    # run("""3,3,1105,-1,9,1101,0,0,12,4,12,99,1""")

    # run("""3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99""")


def run(problem_input: str) -> None:
    program = problem_input.split(",")
    opcode_length = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 99: 1}

    program_counter = 0
    while True:
        opcode_data = str(program[program_counter]).rjust(2, "0")
        opcode = opcode_decoder(opcode_data)
        parameter_data = program[program_counter + 1:program_counter + opcode_length[opcode]]
        parameters = fetch_parameters(opcode, list(opcode_data[:-2][::-1]), program, *map(int, parameter_data))
        program_counter = process(opcode, *parameters, worktape=program, pc=program_counter)
        if program_counter == -1:
            break


def read_file():
    with open('day5.txt', 'r') as f:
        return f.read()


if __name__ == '__main__':
    part_1()

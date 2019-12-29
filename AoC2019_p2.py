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

def main():
	noun, verb = part_2()

	print(noun, verb, noun*100+verb)

def part_2():
	for noun in range(0, 99):
		for verb in range(0, 99):
			if run(noun, verb) == 19690720:
				return (noun, verb)

def run(noun, verb):
	p1_input = read_file()
	program = list(map(int, p1_input.split(",")))
	program[1] = noun
	program[2] = verb

	current = 0
	while(process(program[current], program[current + 1], program[current + 2], program[current + 3], program)):
		current += 4

	return program[0]


def read_file():
	with open('AoC2019_p2_p1.txt', 'r') as f:
		return f.read()

if __name__ == '__main__':
	main()
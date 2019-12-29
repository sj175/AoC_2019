def main():
	print(part_1(read_file()))

def distance(point):
	return abs(point[0]) + abs(point[1])

def get_points(wire):
	switcher = {'R': lambda x, y: (x[0] + y, x[1]), 'L': lambda x, y: (x[0] - y, x[1]), 'U': lambda x, y: (x[0], x[1] + y), 'D': lambda x, y: (x[0], x[1] - y)}
	points = set() # self overlaps don't matter
	current = (0, 0)
	for instruction in wire:
		for _ in range(int(instruction[1:])):
			current = switcher[instruction[0]](current, 1)
			points.add(current)

	# print("POINTS: ", points)
	return points

def part_1(problem):
	wire1, wire2 = problem.split("\n")[:-1]
	wire1 = wire1.split(",")
	wire2 = wire2.split(",")

	wire1_points = get_points(wire1)
	wire2_points = get_points(wire2)

	intersection = set()

	for point in wire2_points:
		if point in wire1_points:
			intersection.add(point)

	# print(wire2_points, "***", wire1_points, "INTER", intersection)

	return min(map(distance, intersection))

def get_points_with_counter(wire):
	switcher = {'R': lambda x, y: (x[0] + y, x[1]), 'L': lambda x, y: (x[0] - y, x[1]), 'U': lambda x, y: (x[0], x[1] + y), 'D': lambda x, y: (x[0], x[1] - y)}
	points = set() # self overlaps don't matter
	current = (0, 0)
	counter = 0
	for instruction in wire:
		for _ in range(int(instruction[1:])):
			counter += 1
			current = switcher[instruction[0]](current, 1)
			points.add((current, counter))

	# print("POINTS: ", points)
	return points

def part_2():
	pass


def read_file():
	with open('AoC2019_p3_p1.txt', 'r') as f:
		return f.read()

if __name__ == '__main__':
	main()
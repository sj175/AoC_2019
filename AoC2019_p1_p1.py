def fuel_cost_2(mass):
	fuel_mass = int(mass) // 3 - 2
	if fuel_mass <= 0:
		return 0

	return fuel_mass + fuel_cost_2(fuel_mass)

def fuel_cost(mass):
	return int(mass) // 3 - 2

def main():
	p1_input = read_file()
	sum = 0
	for line in p1_input.split("\n")[:-1]:
		sum += fuel_cost_2(line)

	print(sum)



def read_file():
	with open('AoC2019_p1_p1.txt', 'r') as f:
		return f.read()

if __name__ == '__main__':
	main()
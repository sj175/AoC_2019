from typing import List, Tuple


def read_input() -> str:
    with open('day6.txt', 'r') as f:
        return f.read()


def find_root(lines: List[str]) -> str:
    # not actually necessary the question tells you it will be COM
    lefts = [line.split(")")[0] for line in lines]
    rights = [line.split(")")[1] for line in lines]

    for possible in lefts:
        if possible not in rights:
            return possible

    return ""


def find_links(to: str, lines: List[str]) -> List[str]:
    output = []

    for line in lines:
        if line.split(")")[0] == to:
            output.append(line.split(")")[1])

    return output


def find_orbital_parent(of: str, lines: List[str]) -> str:
    for line in lines:
        if line.split(")")[1] == of:
            return line.split(")")[0]

    return ""


def find_links_both_directions(to: str, lines: List[str]) -> List[str]:
    output = []

    for line in lines:
        if line.split(")")[0] == to:
            output.append(line.split(")")[1])
        if line.split(")")[1] == to:
            output.append(line.split(")")[0])

    return output


def part_1(problem_input: str) -> int:
    lines = problem_input.split("\n")
    root = "COM"
    graph = {}
    to_visit: List[Tuple[str, int]] = [(root, 0)]
    total = 0
    while to_visit:
        current = to_visit[0]
        to_visit = to_visit[1:]
        count = current[1]
        total += count
        links = find_links(current[0], lines)
        graph[current] = links
        for node in links:
            to_visit.append((node, count + 1))

    return total


def part_2(problem_input: str, start: str, end: str) -> int:
    lines = problem_input.split("\n")
    start = find_orbital_parent(start, lines)
    end = find_orbital_parent(end, lines)

    to_visit = [(start, 0)]
    while to_visit:
        current = to_visit[0]
        to_visit = to_visit[1:]
        count = current[1]
        if current[0] == end:
            return count
        links = find_links_both_directions(current[0], lines)
        for node in links:
            to_visit.append((node, count + 1))

    return 0


def main():
    print(part_1("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""") == 42)

    print(part_1(read_input()))

    print(part_2("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""", "YOU", "SAN"))

    #print(part_2(read_input(), "YOU", "SAN"))


if __name__ == '__main__':
    main()

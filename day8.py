from typing import List, Tuple
from itertools import zip_longest


def read_input() -> str:
    with open('day8.txt', 'r') as f:
        return f.read()


def grouper(n, iterable, fillvalue=None):
    """grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"""
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def layer_count(layer: List[Tuple[int, ...]], x: str) -> int:
    total = 0
    for row in layer:
        total += row.count(x)

    return total


def part_1(problem_input: str, width=25, height=6) -> int:
    layers = list(grouper(height, list(grouper(width, problem_input))))

    my_min = 999999999
    min_layer = ()
    for layer in layers:
        if layer_count(layer, "0") < my_min:
            my_min = layer_count(layer, "0")
            min_layer = layer

    return layer_count(min_layer, "1") * layer_count(min_layer, "2")


if __name__ == '__main__':
    print(part_1(read_input(), 25, 6))

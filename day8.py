from typing import List, Tuple
from itertools import zip_longest
import numpy as np
from PIL import Image


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
    min_layer: List[Tuple[int, ...]] = [()]
    for layer in layers:
        if layer_count(layer, "0") < my_min:
            my_min = layer_count(layer, "0")
            min_layer = layer

    return layer_count(min_layer, "1") * layer_count(min_layer, "2")


def part_2(problem_input: str, width=25, height=6) -> List[List[int]]:
    layers = list(grouper(height, list(grouper(width, problem_input))))

    final_layer = [[-1] * 25 for _ in range(6)]

    for layer in layers:
        for y in range(height):
            for x in range(width):
                if layer[y][x] != '2':
                    if final_layer[y][x] == -1:
                        final_layer[y][x] = int(layer[y][x])

    return final_layer


def plebbing(inp: List[List[int]]) -> List[List[Tuple[int, int, int]]]:
    output = [[-1]*25 for _ in range(6)]

    for y in range(6):
        for x in range(25):
            if inp[y][x] == 0:
                output[y][x] = (255, 255, 255)
            elif inp[y][x] == 1:
                output[y][x] = (0, 0, 0)
            else:
                print("fuck")

    return output


if __name__ == '__main__':
    print(part_1(read_input(), 25, 6))

    img = Image.fromarray(np.asarray(plebbing(part_2(read_input())), dtype=np.uint8))
    img.save('day8.png')

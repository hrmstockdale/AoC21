from pathlib import Path
from typing import Iterable
from operator import add, sub

from utils.read import read_file_iter

MAPPING = {"forward": add, "down": add, "up": sub}


def solver(input: Iterable[str]) -> str:
    depth = 0
    horizontal = 0
    for i in input:
        instruction, _, num = i.partition(" ")
        num = int(num)
        if instruction == "forward":
            horizontal = MAPPING[instruction](horizontal, num)
        else:
            depth = MAPPING[instruction](depth, num)
    return depth * horizontal


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input.txt"
    input_iter = read_file_iter(input_path)

    # Use the following line instead if the input is a single line
    # print(solver(next(input_iter)), end="")
    print(solver(input_iter), end="")

# noinspection PyUnresolvedReferences
import numpy as np


def part1(input: str) -> int:
    for index in range(len(input)):
        if len(set(input[index:index + 4])) == 4:
            return index + 4
    assert False


def part2(input: str) -> int:
    for index in range(len(input)):
        if len(set(input[index:index + 14])) == 14:
            return index + 14
    assert False


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", part1(input))
    print("Result of part 2 is", part2(input))

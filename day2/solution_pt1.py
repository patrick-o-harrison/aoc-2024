def solution(data):
    lines = [[int(f) for f in line.split(' ')] for line in data.split('\n')]
    return sum((line_valid(line) for line in lines))


def line_valid(line):
    from itertools import pairwise

    if line[0] < line[1]:

        def validator(a, b):
            return a < b and b - a <= 3

    elif line[0] > line[1]:

        def validator(a, b):
            return a > b and a - b <= 3

    else:
        return False
    return all(validator(*pair) for pair in pairwise(line))


def test_solution():
    import textwrap

    data = textwrap.dedent(
        """\
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9"""
    )
    value = solution(data)
    assert value == 2


if __name__ == "__main__":
    import sys

    f = open(sys.argv[1], "r")
    data = f.read()
    value = solution(data.strip())
    print(value)

def solution(data):
    lines = parse_input_data(data)
    valid_line_count = 0
    for line in lines:
        modified_lines = all_modified_lines(line)
        for modified_line in modified_lines:
            if line_is_valid(modified_line):
                valid_line_count += 1
                break
    return valid_line_count


def parse_input_data(data):
    data = data.strip()
    return [
        [int(text_num) for text_num in text_line.split(" ")]
        for text_line in data.split("\n")
    ]


def modified_line(line, i):
    modified_line = line.copy()
    modified_line.pop(i)
    return modified_line


def all_modified_lines(line):
    yield line
    for i in range(len(line)):
        yield modified_line(line, i)


def valid_lt_pair(a, b):
    return a < b and b - a <= 3


def valid_gt_pair(a, b):
    return a > b and a - b <= 3


def line_is_valid(line, retried=False):
    from itertools import pairwise

    if line[0] < line[1]:
        valid_pair = valid_lt_pair
    elif line[0] > line[1]:
        valid_pair = valid_gt_pair
    else:
        return False
    return all(valid_pair(*pair) for pair in pairwise(line))


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
    assert value == 4


if __name__ == "__main__":
    import sys

    f = open(sys.argv[1], "r")
    data = f.read()
    value = solution(data)
    print(value)

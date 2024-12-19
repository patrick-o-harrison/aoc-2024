def solution(data):
    import re

    result = 0
    for match in re.finditer(r"mul\((\d+),(\d+)\)", data):
        a = int(match.groups()[0])
        b = int(match.groups()[1])
        result += a * b

    return result


def test_solution():
    data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    value = solution(data)
    assert value == 161


if __name__ == "__main__":
    import sys

    f = open(sys.argv[1], "r")
    data = f.read()
    value = solution(data.strip())
    print(value)

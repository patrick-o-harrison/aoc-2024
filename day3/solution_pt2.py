def solution(data):
    result = 0

    doing = True
    for instruction in parse_data(data):
        op = instruction[0]
        if op == "mul" and doing:
            result += instruction[1] * instruction[2]
        elif op == "do":
            doing = True
        elif op == "dont":
            doing = False

    return result


def parse_data(data):
    import re

    pattern = re.compile(
        r"(?P<mul>mul)\((?P<a>\d+),(?P<b>\d+)\)|(?P<do>do\(\))|(?P<dont>don't\(\))"
    )
    for match in re.finditer(pattern, data):
        yield process_match(match)


def process_match(match):
    groups = match.groupdict()
    if groups["mul"] is not None:
        return ("mul", int(groups["a"]), int(groups["b"]))
    elif groups["do"] is not None:
        return ("do",)
    elif groups["dont"] is not None:
        return ("dont",)
    else:
        return (None,)


def test_solution():
    data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    value = solution(data)
    assert value == 48


if __name__ == "__main__":
    import sys

    f = open(sys.argv[1], "r")
    data = f.read()
    value = solution(data.strip())
    print(value)

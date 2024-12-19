def solution(f):
    lines = (line.strip() for line in f.readlines())
    pairs = (map(int, line.split("   ")) for line in lines)
    sorted_pairs = zip(*map(sorted, zip(*pairs)))
    differences = (abs(pair[0] - pair[1]) for pair in sorted_pairs)
    return sum(differences)


def test_solution():
    import textwrap
    from io import StringIO

    input_data = textwrap.dedent(
        """\
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3"""
    )
    sf = StringIO(input_data)
    sf.seek(0)
    value = solution(sf)
    assert value == 11


if __name__ == "__main__":
    import sys

    input_fname = sys.argv[1]
    file = open(input_fname, "r")
    value = solution(file)
    print(value)

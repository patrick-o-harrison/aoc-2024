def solution(f):
    from collections import Counter
    lines = (line.strip() for line in f.readlines())
    pairs = (map(int, line.split("   ")) for line in lines)
    la, lb = zip(*pairs)
    freq = Counter(lb)
    similarities = (li * freq.get(li, 0) for li in la)
    return sum(similarities)


def test_solution():
    import textwrap
    from io import StringIO
    input_data = textwrap.dedent("""\
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3""")
    sf = StringIO(input_data)
    sf.seek(0)
    value = solution(sf)
    assert(value == 31)

if __name__ == '__main__':
    import sys
    input_fname = sys.argv[1]
    try:
        file = open(input_fname, 'r')
    except:
        print("Failed to open file.", file=sys.stderr)
        sys.exit(1)
    value = solution(file)
    print(value)

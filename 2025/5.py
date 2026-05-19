data = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()

with open("input.txt", "r") as f:
    data = f.read().strip()

def parse_data(data):
    range_strs, ids = data.split('\n\n')
    ids = [int(x) for x in ids.strip().split()]

    ranges = []
    for s in range_strs.strip().split():
        l, r = s.split('-')
        ranges.append(range(int(l), int(r) + 1))
    
    return ranges, ids

def P1():
    ranges, ids = parse_data(data)
    count = 0
    for i in ids:
        for r in ranges:
            if i in r:
                count += 1
                break

    return count

def P2():
    ranges, _ = parse_data(data)

    # Once I learned that I have to sort the ranges (hint from Gemini).
    # I figured out the rest. So, sorting the ranges collection was a crucial/spoiler hint.
    ranges.sort(key=lambda x: x.start)

    lhs, rhs = ranges[0].start, ranges[0].stop
    count = 0
    for r in ranges[1:]:
        if lhs <= r.start <= rhs:
            rhs = max(r.stop, rhs)
        else:
            count += rhs - lhs
            lhs, rhs = r.start, r.stop

    return (rhs - lhs) + count

print(P2())
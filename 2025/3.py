from itertools import pairwise

data = """
987654321111111
811111111111119
234234234234278
818181911112111
""".strip().split()

with open("input.txt", "r") as f:
    data = f.read().strip().split()

# Part 1
def part_1():
    joltages = []
    for bank in data:
        max_jolt = -1
        for i, lhs in enumerate(bank):
            for j, rhs in enumerate(bank[i+1:]):
                jolt = int(lhs) * 10 + int(rhs)
                if jolt > max_jolt:
                    max_jolt = jolt
        
        joltages.append(max_jolt)
    return joltages

def part_2():
    # written with help from gemini!
    def find_largest_number(seq):
        n = len(seq)
        deletions_left = n - 12

        stack = []

        for digit in map(int, seq):
            while stack and deletions_left > 0 and digit > stack[-1]:
                stack.pop()
                deletions_left -= 1
        
            stack.append(digit)
        
        if deletions_left > 0:
            stack = stack[:-deletions_left]
        
        return int("".join(map(str, stack)))
    return [find_largest_number(bank) for bank in data]

# for j in joltages:
#     print(j)

print(f"Part 1: {sum(part_1())}")
print(f"Part 2: {sum(part_2())}")

from pprint import pprint
from copy import deepcopy

data = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

""".strip().split()

with open("input.txt", "r") as f:
    data = f.read().strip().split()

row_count = len(data) + 2
col_count = len(data[0]) + 2


mod_data = ['*' * col_count] + data + ['*' * col_count]

for i, row in enumerate(mod_data):
    if i in (0, len(mod_data) - 1):
        continue

    mod_data[i] = '*' + row + '*'

data = [list(x) for x in mod_data]

def is_roll_accessible(data, i, j):
        neighbors = [
            data[i][j-1], # left
            data[i][j+1], # right
            data[i-1][j], # up
            data[i+1][j], # down
            data[i-1][j-1], # up left
            data[i-1][j+1], # up right
            data[i+1][j-1], # down left
            data[i+1][j+1], # down right
        ]
        return sum(x == '@' for x in neighbors) < 4

# part 1
def count_accessible_rolls():
    data_ref = deepcopy(data)
    count = 0
    for i in range(1, row_count -1):
        for j in range(1, col_count -1):
            if data[i][j] == '@' and is_roll_accessible(data_ref, i, j):
                count += 1
    return count

def remove_accessible_rolls(debug=True):
    data_ref = deepcopy(data)

    for i in range(1, row_count -1):
        for j in range(1, col_count -1):
            if data[i][j] == '@' and is_roll_accessible(data_ref, i, j):
                data[i][j] = 'x' if debug else '.'

def print_grid(data):
    for i in range(1, row_count -1):
        for j in range(1, col_count - 1):
            print(data[i][j], end='')
        print()
    print()

def P2():
    removable_count = 0

    count = count_accessible_rolls()
    remove_accessible_rolls()
    # print_grid(data)
    # print(f"removed: {count}")
    removable_count += count

    while count > 0:
        count = count_accessible_rolls()
        remove_accessible_rolls()
        # print(f"removed: {count}")
        removable_count += count
    
    return removable_count

print(P2())
import operator
from functools import reduce

data = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip().split('\n')

with open("input.txt", "r") as f:
    data = f.read().strip().split('\n')


def print_mat(mat):
    row_count = len(mat)
    col_count = len(mat[0])

    for i in range(row_count):
        for j in range(col_count):
            print(mat[i][j], end = ' ')
        print()
    print()

def transpose(mat):
    row_count = len(mat)
    col_count = len(mat[0])

    mat_T = [[] for _ in range(col_count)]

    for j in range(col_count):
        for i in range(row_count):
            mat_T[j].append(0)

    for i in range(row_count):
        for j in range(col_count):
            mat_T[j][i] = mat[i][j]
    return mat_T

def P1():
    rows = [r.split() for r in data]
    rows = [rows[-1]] + [[int(x) for x in r] for r in rows[:-1]]

    row_count = len(rows)
    col_count = len(rows[0])

    total = 0
    for j in range(col_count):
        op = rows[0][j]

        if op == '+':
            total += sum(rows[i][j] for i in range(1, row_count))

        if op == '*':
            p = 1
            for i in range(1, row_count):
                p *= rows[i][j]
            total += p
    return total

def P2():
    mat = [list(r) for r in data[:-1]]
    row_count = len(mat)
    col_count = len(mat[0])

    mat_T = transpose(mat)
    operands = ["".join(r) for r in mat_T]

    op_opr_pairs = []
    for op in data[-1].split():
        i = 0
        required_oprs = []
        for opr in operands[i:]:
            if opr.isspace():
                break
            else:
                required_oprs.append(int(opr))
                i += 1

        operands = operands[i+1:]
        op_opr_pairs.append((op, required_oprs))
    
    total = 0
    for op, oprs in op_opr_pairs:
        if op == '+':
            total += reduce(operator.add, oprs)
        if op == '*':
            total += reduce(operator.mul, oprs)

    return total   

print(P2())
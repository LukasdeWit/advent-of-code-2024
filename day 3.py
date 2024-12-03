import re

def one():
    data = [f.strip() for f in open("day 3 input.txt")]
    ops = []
    for line in data:
        for token in re.findall(r"mul\([0-9]+,[0-9]+\)", line):
            ops.append(token)
    total = 0
    for op in ops:
        total += interp_mul(op)
    return total

def interp_mul(token):
    nums = [int(n) for n in re.findall("[0-9]+", token)]
    return nums[0] * nums[1]

def two():
    data = [f.strip() for f in open("day 3 input.txt")]
    ops = []
    for line in data:
        for token in re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line):
            ops.append(token)
    accept = True
    ops_final = []
    while ops:
        op = ops.pop(0)
        if op == "don't()":
            accept = False
        elif op == "do()":
            accept = True
        else:
            if accept:
                ops_final.append(op)
    total = 0
    for op in ops_final:
        total += interp_mul(op)
    return total

print(one())
print(two())

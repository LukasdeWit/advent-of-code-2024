
def one():
    data = [f.strip() for f in open("day 1 input.txt")]
    a, b = [], []
    for line in data:
        a.append(int(line.split()[0]))
        b.append(int(line.split()[1]))
    a.sort()
    b.sort()
    total = 0
    for i in range(len(a)):
        total += abs(a[i] - b[i])
    return total

def two():
    data = [f.strip() for f in open("day 1 input.txt")]
    a, b = [], []
    for line in data:
        a.append(int(line.split()[0]))
        b.append(int(line.split()[1]))
    total = 0
    for num in a:
        total += b.count(num) * num
    return total

print(one())
print(two())

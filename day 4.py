
def one():
    data = [f.strip() for f in open("day 4 input.txt")]
    total = 0
    for i in range(4):
        total += check_hori(data) + check_dia(data)
        data = rotate_90(data)
    return total


def check_hori(data):
    total = 0
    for line in data:
        for n in range(len(line) - 3):
            if line[n] == 'X' and line[n + 1] == 'M' and line[n + 2] == 'A' and line[n + 3] == 'S':
                total += 1
    return total


def check_dia(data):
    total = 0
    for m in range(len(data) - 3):
        for n in range(len(data[m]) - 3):
            if data[m][n] == 'X' and data[m + 1][n + 1] == 'M' and data[m + 2][n + 2] == 'A' and data[m + 3][n + 3] == 'S':
                total += 1
    return total


def rotate_90(matrix):
    new_matrix = []
    for m in reversed(range(len(matrix[0]))):
        line = []
        for n in range(len(matrix)):
            line.append(matrix[n][m])
        new_matrix.append(line)
    return new_matrix


def two():
    data = [f.strip() for f in open("day 4 input.txt")]
    total = 0
    for i in range(4):
        total += check_x(data)
        data = rotate_90(data)
    return total


def check_x(data):
    total = 0
    for m in range(1, len(data) - 1):
        for n in range(1, len(data[0]) - 1):
            if data[m][n] == 'A' and data[m - 1][n - 1] == 'M' and data[m - 1][n + 1] == 'M' and \
                data[m + 1][n - 1] == 'S' and data[m + 1][n + 1] == 'S':
                total += 1
    return total


print(one())
print(two())

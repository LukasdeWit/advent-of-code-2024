
def one():
    data = [f.strip() for f in open("day 6 input.txt")]

    lab_map = make_map(data)
    lab_map, _ = run_the_maze(lab_map)
    total = 0
    for line in lab_map:
        for room in line:
            if room == 'X':
                total += 1
    return total


def run_the_maze(lab_map):
    x_pos, y_pos, x_dir, y_dir = 0, 0, 0, -1

    # map direction == map[y][x]
    for n in range(len(lab_map)):
        for m in range(len(lab_map[0])):
            if lab_map[n][m] == '^':
                x_pos, y_pos = m, n
    stepping = True
    corners = {}
    while x_pos + x_dir in range(len(lab_map[0])) and y_pos + y_dir in range(len(lab_map)):
        if lab_map[y_pos + y_dir][x_pos + x_dir] == '#':
            if not (x_pos, y_pos) in corners:
                corners[(x_pos, y_pos)] = []
            if (x_dir, y_dir) in corners[(x_pos, y_pos)]:
                return lab_map, False
            corners[(x_pos, y_pos)].append((x_dir, y_dir))
            x_dir, y_dir = -1 * y_dir, x_dir  # clockwise 1/2pi rotation
        else:
            lab_map[y_pos][x_pos] = 'X'
            x_pos += x_dir
            y_pos += y_dir
    lab_map[y_pos][x_pos] = 'X'
    return lab_map, True


def two():
    data = [f.strip() for f in open("day 6 input.txt")]

    lab_map = make_map(data)
    # run the maze normally
    lab_map, _ = run_the_maze(lab_map)
    total = 0
    for n in range(len(lab_map)):
        for m in range(len(lab_map[0])):
            if lab_map[n][m] == 'X':
                new_map = make_map(data)
                new_map[n][m] = '#'
                new_map, finished = run_the_maze(new_map)
                if not finished:
                    total += 1
    return total



def make_map(data):
    lab_map = []
    for line in data:
        lab_map.append([c for c in line])
    return lab_map


# method only made after one() was already finished, not putting it in
def spin_right(x, y):
    return -1 * y, x


print(one())
print(two())

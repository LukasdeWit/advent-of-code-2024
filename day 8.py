
def one():
    data = [f.strip() for f in open("day 8 input.txt")]
    nodes = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] != '.':
                if data[y][x] not in nodes:
                    nodes[data[y][x]] = []
                nodes[data[y][x]].append((x, y))
    x_bound = len(data[0])
    y_bound = len(data)

    antinodes = []
    for node_type in nodes:
        if len(nodes[node_type]) >= 2:
            for node_n in range(len(nodes[node_type]) - 1):
                node_1 = nodes[node_type][node_n]
                for node_2 in nodes[node_type][node_n + 1:]:
                    x_diff = node_2[0] - node_1[0]
                    y_diff = node_2[1] - node_1[1]
                    if not (node_1[0] - x_diff, node_1[1] - y_diff) in antinodes and \
                        in_bounds(node_1[0] - x_diff, node_1[1] - y_diff, x_bound, y_bound):
                        antinodes.append((node_1[0] - x_diff, node_1[1] - y_diff))
                    if not (node_2[0] + x_diff, node_2[1] + y_diff) in antinodes and \
                        in_bounds(node_2[0] + x_diff, node_2[1] + y_diff, x_bound, y_bound):
                        antinodes.append((node_2[0] + x_diff, node_2[1] + y_diff))
    return len(antinodes)


def in_bounds(x_pos, y_pos, x_bound, y_bound):
    return 0 <= x_pos < x_bound and 0 <= y_pos < y_bound


def two():
    data = [f.strip() for f in open("day 8 input.txt")]
    nodes = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] != '.':
                if data[y][x] not in nodes:
                    nodes[data[y][x]] = []
                nodes[data[y][x]].append((x, y))
    x_bound = len(data[0])
    y_bound = len(data)

    antinodes = []
    for node_type in nodes:
        if len(nodes[node_type]) >= 2:
            for node_n in range(len(nodes[node_type]) - 1):
                node_1 = nodes[node_type][node_n]
                for node_2 in nodes[node_type][node_n + 1:]:
                    for loc in calc_positions(node_1, node_2, x_bound, y_bound):
                        if not loc in antinodes:
                            antinodes.append(loc)
    return len(antinodes)


def calc_positions(pos_1, pos_2, x_bound, y_bound):
    locations = []
    x_diff, y_diff = pos_1[0] - pos_2[0], pos_1[1] - pos_2[1]
    # move back from position 1
    x_pos, y_pos = pos_1
    while in_bounds(x_pos, y_pos, x_bound, y_bound):
        locations.append((x_pos, y_pos))
        x_pos -= x_diff
        y_pos -= y_diff
    # move forward from position 2
    x_pos, y_pos = pos_2
    while in_bounds(x_pos, y_pos, x_bound, y_bound):
        locations.append((x_pos, y_pos))
        x_pos += x_diff
        y_pos += y_diff
    return locations


print(one())
print(two())

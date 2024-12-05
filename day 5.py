
def one():
    data = [f.strip() for f in open("day 5 input.txt")]
    rules = {}
    item = data.pop(0)
    while item != '':
        if item.split('|')[0] not in rules:
            rules[item.split('|')[0]] = []
        rules[item.split('|')[0]].append(item.split('|')[1])
        item = data.pop(0)
    correct_data = []
    for line in data:
        if check_rules(rules, line.split(',')):
            correct_data.append(line)
    total = 0
    for entry in correct_data:
        middle = len(entry.split(',')) // 2
        total += int(entry.split(',')[middle])
    return total


def check_rules(rules, line):
    for n in range(len(line) - 1):
        for c in range(n + 1, len(line)):
            if line[n] not in rules or not line[c] in rules[line[n]]:
                return False
    return True


def two():
    data = [f.strip() for f in open("day 5 input.txt")]
    rules = {}
    item = data.pop(0)
    while item != '':
        if item.split('|')[0] not in rules:
            rules[item.split('|')[0]] = []
        if item.split('|')[1] not in rules:
            rules[item.split('|')[1]] = []
        rules[item.split('|')[0]].append(item.split('|')[1])
        item = data.pop(0)
    incorrect_data = []
    for line in data:
        if not check_rules(rules, line.split(',')):
            incorrect_data.append(line)
    total = 0
    for line in incorrect_data:
        entry = line.split(',')
        sorted_entry = ins_sort(rules, entry)
        middle = len(sorted_entry) // 2
        total += int(sorted_entry[middle])
    return total


def ins_sort(rules, data):
    sorted_data = [data.pop()]
    while data:
        entry = data.pop()
        for n in range(len(sorted_data)):
            if not entry in rules[sorted_data[n]]:
                sorted_data.insert(n, entry)
                break
        if not entry in sorted_data:
            sorted_data.append(entry)
    return sorted_data


print(one())
print(two())

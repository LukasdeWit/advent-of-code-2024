
def one():
    data = [f.strip() for f in open("day 7 input.txt")]

    total = 0
    for line in data:
        ans, nums = line.split(': ')
        problems = insert_operations_one(nums.split(' '))
        for prob in problems:
            if int(ans) == eval(prob):
                total += int(ans)
                break
    return total


def insert_operations_one(numbers):
    if len(numbers) == 2:
        return [f"({numbers[0]} + {numbers[1]})", f"({numbers[0]} * {numbers[1]})"]
    problems = []
    for prob in insert_operations_one([f"({numbers[0]} + {numbers[1]})"] + numbers[2:]):
        problems.append(prob)
    for prob in insert_operations_one([f"({numbers[0]} * {numbers[1]})"] + numbers[2:]):
        problems.append(prob)
    return problems


def two():
    data = [f.strip() for f in open("day 7 input.txt")]

    total = 0
    for line in data:
        ans, pre_problems = line.split(': ')
        numbers = [int(n.strip()) for n in pre_problems.split(' ')]
        if int(ans) in insert_operations_two(numbers):
            total += int(ans)
    return total


def insert_operations_two(numbers):
    if len(numbers) == 2:
        return [numbers[0] + numbers[1], numbers[0] * numbers[1], int(f"{numbers[0]}{numbers[1]}")]
    final_answers = []
    for prob in insert_operations_two([numbers[0] + numbers[1]] + numbers[2:]):
        final_answers.append(prob)
    for prob in insert_operations_two([numbers[0] * numbers[1]] + numbers[2:]):
        final_answers.append(prob)
    for prob in insert_operations_two([int(f"{numbers[0]}{numbers[1]}")] + numbers[2:]):
        final_answers.append(prob)
    return final_answers


print(one())
print(two())

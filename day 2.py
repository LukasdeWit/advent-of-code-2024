
def one():
    data = [f.strip() for f in open("day 2 input.txt")]
    total = 0
    for line in data:
        nums = [int(n) for n in line.split()]
        if safe_asc(nums) or safe_desc(nums):
            total += 1
    return total

def safe_asc(nums):
    for n in range(len(nums) - 1):
        if not (nums[n + 1] > nums[n] and nums[n + 1] - nums[n] in [1, 2, 3]):
            return False
    return True

def safe_desc(nums):
    for n in range(len(nums) - 1):
        if not (nums[n + 1] < nums[n] and nums[n] - nums[n + 1] in [1, 2, 3]):
            return False
    return True

def two():
    data = [f.strip() for f in open("day 2 input.txt")]
    total = 0
    for line in data:
        dampened = dampen([int(n) for n in line.split()])
        safe = False
        for nums in dampened:
            if safe_asc(nums) or safe_desc(nums):
                safe = True
        if safe:
            total += 1
    return total

def dampen(nums):
    dampened = []
    for i in range(len(nums)):
        dampened.append([n for n in nums])
        dampened[i].pop(i)
    return dampened

print(one())
print(two())

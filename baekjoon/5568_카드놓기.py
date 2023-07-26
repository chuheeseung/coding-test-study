import itertools

n = int(input())
k = int(input())
numbers = []
dicts = {}

for _ in range(n):
    numbers.append((input()))

cases = list(itertools.permutations(numbers, k))

for case in cases:
    num = ''.join(case)

    if num in dicts:
        dicts[num] += 1
    else:
        dicts[num] = 1

print(len(dicts))

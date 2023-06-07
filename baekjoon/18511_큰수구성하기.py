import sys
from itertools import product
input = sys.stdin.readline

n, k = map(int, input().split())
k_list = list(input().split())
results = []

for i in range(1, k + 1):
    cases = list(product(k_list, repeat=i))

    for case in cases:
        number = ''.join(map(str, case))
        if int(number) <= n:
            results.append(int(number))


print(max(results))
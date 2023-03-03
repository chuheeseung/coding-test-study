from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cases = list(combinations(cards, 3))
maxSum = 0

for case in cases:
    caseSum = sum(case)

    if caseSum <= m:
        maxSum = max(maxSum, caseSum)
    else:
        continue

print(maxSum)

'''
5 21
5 6 7 8 9 / 21

10 500
93 181 245 214 315 36 185 138 216 295 / 497
'''
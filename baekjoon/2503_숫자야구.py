from itertools import permutations

n = int(input())
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data, 3))

for _ in range(n):
    n, s, b = map(int, input().split())
    n = list(str(n))
    rmcnt = 0

    for i in range(len(num)):
        strike = ball = 0
        i -= rmcnt # 조합 리스트의 처음 원소부터 비교해주기 위해서 i 인덱스를 0부터 시작하도록 해줌

        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1

        if (strike != s) or (ball != b):
            num.remove(num[i])
            rmcnt += 1

print(len(num))


'''
4
123 1 1
356 1 0
327 2 0
489 0 1
'''
from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
count = 0
dic = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        flag = 0

        if j in dic[i]:
            flag = 1

        for k in range(j + 1, n + 1):
            if flag == 0 and k not in dic[i] and k not in dic[j]:
                count += 1

print(count)
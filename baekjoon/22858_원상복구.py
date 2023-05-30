n, k = map(int, input().split())
s = list(map(int, input().split()))
d_temp = list(map(int, input().split()))
result = [s[i] for i in range(n)]

d = []

for i in range(n):
    d.append([d_temp[i], i])

d.sort()

for i in range(k):
    temp = []

    for di in d:
        temp.append(result[di[1]])
    for j in range(n):
        result[j] = temp[j]

print(*result)

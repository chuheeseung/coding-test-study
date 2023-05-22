n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = [0] * (n + m)

for i in range(n):
    result[i] = a[i]

for j in range(m):
    result[j+n] = b[j]

for i in sorted(result):
    print(i, end=' ')
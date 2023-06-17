n, k = map(int, input().split())
m = list(map(int, input().split()))
m = m + m[::-1]

for i in range(n * 2):
    k -= m[i]

    if k < 0:
        if i > n:
            print((n * 2) - i)
            break
        else:
            print(i + 1)
            break

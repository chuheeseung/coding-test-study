n, m = map(int, input().split())
lights = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        lights[b-1] = c
    elif a == 2:
        for i in range(b, c + 1):
            lights[i-1] = 1 - lights[i-1]
    elif a == 3:
        for i in range(b, c + 1):
            lights[i-1] = 0
    else:
        for i in range(b, c + 1):
            lights[i-1] = 1

print(*lights)
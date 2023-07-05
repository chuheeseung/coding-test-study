import sys
input = sys.stdin.readline

n = int(input())
planet = list(map(int, input().split()))
speed = planet[-1]

for i in range(n - 2, -1, -1):
    if planet[i] < speed:
        if speed % planet[i] == 0:
            continue
        speed = ((speed // planet[i]) + 1) * planet[i]
    else:
        speed = planet[i]

print(speed)
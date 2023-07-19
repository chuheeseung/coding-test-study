import sys
import math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
no = []

for i in range(n):
    gcd = math.gcd(a[i], x)

    if gcd == 1:
        no.append(a[i])

print(sum(no) / len(no))
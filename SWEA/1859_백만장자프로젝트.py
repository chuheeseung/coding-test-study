t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    result = 0
    max_num = 0

    for i in range(len(prices)-1, -1, -1):

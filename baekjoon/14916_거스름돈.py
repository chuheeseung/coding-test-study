n = int(input())
coins = 0

while True:
    if n % 5 == 0:
        coins += n // 5
        break
    else:
        n -= 2
        coins += 1

    if n < 0:
        break

if n < 0:
    print(-1)
else:
    print(coins)

'''
13
14

5
4
'''
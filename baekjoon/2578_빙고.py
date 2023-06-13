import sys
input = sys.stdin.readline

c = [list(map(int, input().split())) for _ in range(5)]
mc = []
count = 0

for _ in range(5):
    mc += list(map(int, input().split()))


def check():
    bingo = 0

    for x in c:
        if x.count(0) == 5:
            bingo += 1

    for i in range(5):
        y = 0
        for j in range(5):
            if c[j][i] == 0:
                y += 1

        if y == 5:
            bingo += 1

    d1 = 0
    for i in range(5):
        if c[i][i] == 0:
            d1 += 1

    if d1 == 5:
        bingo += 1

    d2 = 0
    for i in range(5):
        if c[i][4 - i] == 0:
            d2 += 1

    if d2 == 5:
        bingo += 1

    return bingo


for i in range(25):
    for x in range(5):  # 2차원 배열은 for x, for y로 이중으로 도는 걸 생각하자
        for y in range(5):
            if mc[i] == c[x][y]:
                c[x][y] = 0
                count += 1

    if count >= 12:
        result = check()

        if result >= 3:
            print(i + 1)
            break

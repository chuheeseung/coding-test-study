c = int(input())

for _ in range(c):
    cases = list(map(int, input().split()))
    average = sum(cases[1:]) / cases[0]
    count = 0

    for s in cases[1:]:
        if s > average:
            count += 1

    rate = count / cases[0] * 100
    print(f'{rate:.3f}%')


'''
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

40.000%
57.143%
33.333%
66.667%
55.556%
'''
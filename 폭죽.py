t = int(input())

for test_case in range(1, t + 1):
    n, d = map(int, input().split())
    time = []

    for _ in range(n):
        time.append(list(map(int, input().split())))

    left_location = 0
    left_delay = 0
    right_location = 0
    right_delay = 0

    for i in range(n):
        if d - time[i][0] >= time[i][0]:
            left_location += time[i][0]
            left_delay += time[i][1]
        else:
            right_location += time[i][0]
            right_delay += time[i][1]
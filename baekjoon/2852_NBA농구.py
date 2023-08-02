import sys
input = sys.stdin.readline

n = int(input())
score = {1: 0, 2: 0}
time = {1: 0, 2: 0}
answer = {1: 0, 2: 0}
state = 0
# 0 : 동점
# 1 : 1팀이 이기고 있음
# 2 : 2팀이 이기고 있음

for _ in range(n):
    team, t = input().split()
    team = int(team)
    m, s = map(int, t.split(':'))
    t = m * 60 + s
    score[team] += 1

    if state == 0:
        time[team] = t
        state = team
    elif state != 0 and score[1] == score[2]:
        answer[state] += t - time[state]
        state = 0

if state != 0:
    answer[state] += 60 * 48 - time[state]

print('{:0>2}:{:0>2}'.format(answer[1]//60, answer[1] % 60))
print('{:0>2}:{:0>2}'.format(answer[2]//60, answer[2] % 60))
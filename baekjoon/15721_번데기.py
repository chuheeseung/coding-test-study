a = int(input())
t = int(input())
x = int(input()) # 0: 뻔, 1: 데기

bundegi = [] # (번/데기 횟수, 번/데기 구분) 튜플을 원소로 갖는 리스트
bun = 1 # 번을 외친 횟수
degi = 1 # 데기를 외친 횟수
turn = 0 # 게임의 회차 수

while True:
    previous_n = bun # 이전 회차에서 번데기를 외친 누적 횟수를 저장
    turn += 1

    for _ in range(2): # 번 - 데기 - 번 - 데기
        bundegi.append((bun, 0))
        bun += 1
        bundegi.append((degi, 1))
        degi += 1

    for _ in range(turn + 1): # 번 * (turn+1)
        bundegi.append((bun, 0))
        bun += 1

    for _ in range(turn + 1): # n회차일 때 번/데기 연속 n+1번 기록
        bundegi.append((degi, 1))
        degi += 1

    if previous_n < t <= bun: # 구하고자 하는 t가 이번 회차에 있는 경우
        print(bundegi.index((t, x)) % a) # 총 누적 수 % 인원 수
        break
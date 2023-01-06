def solution(progresses, speeds):
    answer = []

    while progresses: # 작업리스트가 빌 때까지 반복
        cnt = 0 # 몇개의 기능이 배포되었는지 저장

        while progresses and progresses[0] >= 100:
            # 작업리스트가 남아있고, 맨 앞의 작업 진도가 100인 경우
            # -> 기능 배포 변수 + 1, 해당 작업, 작업속도를 리스트에서 제거
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)

        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        # 작업리스트의 진도 증가

        if cnt: # 오늘 기능 배포될 게 생기면 결과 리스트에 추가
            answer.append(cnt)

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
answer = solution(progresses, speeds)
print(answer)
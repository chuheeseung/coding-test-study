def solution(priorities, location):
    answer = 0

    while True:
        max_num = max(priorities) # 가장 큰 중요도

        for i in range(len(priorities)):
            if max_num == priorities[i]: # max_num과 리스트 요소가 일치하는 경우
                answer += 1 # 프린트했다고 간주 -> answer + 1
                priorities[i] = 0 # 프린트했으니까 0으로 값 갱신
                max_num = max(priorities) # 가장 큰 중요도 다시 갱신

                if i == location: # 찾고자 하는 위치이면 바로 answer 값 반환
                    return answer

priorities = [2, 1, 3, 2]
location = 2
answer = solution(priorities, location)
print(answer)
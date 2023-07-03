n = int(input())
n_list = list(map(int, input().split()))
max_length = 2
count = 2

for i in range(n - 2):
    if n_list[i] <= n_list[i + 1] <= n_list[i + 2]:
        count = 2
    elif n_list[i] >= n_list[i + 1] >= n_list[i + 2]:
        count = 2
    else:
        count += 1

    max_length = max(max_length, count)

print(max_length)

'''
- max_length = 2로 선언 : 지그재그 수열을 만족하지 않으면 최소 수열의 길이는 2
- count 값 변경 : 연속으로 증감하는 경우에는 count = 2, 아닌 경우에는 count + 1
- max(max_length, count) : 수열의 길이를 계속 갱신
- for i in range(n - 2): 수열의 최소 길이가 2니까 범위를 (n - 2)까지로 설정
- 연속으로 증감 판단 : n_list[i] <= n_list[i+1] <= n_list[i+2] 이렇게 풀면 된다
'''
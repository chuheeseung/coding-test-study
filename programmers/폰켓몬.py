def solution(nums):
    choose = int(len(nums) / 2)
    nums = set(nums) # 개수에 상관없이 set으로 중복을 제거
    answer = min(len(nums), choose)

    return answer


nums = [3, 1, 2, 3]
# nums = [3,3,3,2,2,4]
# nums = [3,3,3,2,2,2]
answer = solution(nums)
print(answer)
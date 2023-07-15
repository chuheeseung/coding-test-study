'''
target: 찾고자 하는 값
data : 오름차순으로 정렬된 리스트
start : data의 처음 값 인덱스
end : data의 마지막 값 인덱스
mid : start, end의 중간값 인덱스

data 중에서 target을 검색해서 index 값을 리턴
'''

def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None

def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search_recursion(target, start, end, data)


# 테스트용 코드
if __name__ == "__main__":
    li = [i ** 2 for i in range(11)]
    target = 9
    idx = binary_search(target, li)
    # idx = binary_search_recursion(target, 0, 10, li)


    if idx:
        print(li[idx])
    else:
        print("{}가 없습니다.".format(target))
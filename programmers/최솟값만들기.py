def solution(a, b):
    answer = 0

    a.sort(reverse=True)
    b.sort()

    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer


A = [1, 4, 2]
B = [5, 4, 4]

# A = [1, 2]
# B = [3, 4]

print(solution(A, B))

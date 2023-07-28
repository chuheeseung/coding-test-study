n = int(input()) # 도시의 개수
roads = list(map(int, input().split()))  # 도시의 길이
costs = list(map(int, input().split())) # 주유소 리터 당 가격

# 도시를 넘어가려면 기름이 반드시 있어야 함 -> 첫번째에서 주유를 해야함
res = roads[0] * costs[0] # 도시2로 가는 길이 * 도시1 리터 당 가격
m = costs[0]
dist = 0

for i in range(1, n - 1):
    if costs[i] < m: # 지금까지의 주유 가격보다 이번 도시에서의 가격이 작은 경우
        res += m * dist # 지금까지의 거리 * 가장 작은 주유 가격 을 더해줌
        dist = roads[i]
        m = costs[i] 
    else:
        dist += roads[i]

    if i == n - 2:
        res += m * dist

print(res)
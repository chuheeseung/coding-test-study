t = int(input())

for _ in range(t):
    j, n = map(int, input().split())
    boxes = []
    count = 0

    for _ in range(n):
        r, c = map(int, input().split())
        boxes.append([r * c, r, c])

    boxes.sort(reverse=True)

    for box in boxes:
        if j <= 0:
            break
        else:
            j -= box[0]
            count += 1

    print(count)




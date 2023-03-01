n = int(input())
score = list(map(int, input().split()))
new_scores = []
average = 0

for s in score:
    new = s / max(score) * 100
    new_scores.append(new)

average = sum(new_scores) / len(new_scores)
print(average)


'''
3
40 80 60 / 75.0

3
10 20 30 / 66.666667

4
1 100 100 100 / 75.25

5
1 2 4 8 16 / 38.75

2
3 10 / 65.0

4
10 20 0 100 / 32.5

1
50 / 100.0

9
10 20 30 40 50 60 70 80 90 / 55.55555555555556
'''
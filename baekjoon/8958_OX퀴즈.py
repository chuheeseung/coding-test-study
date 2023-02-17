t = int(input())

for _ in range(t):
    quiz = list(input())
    score = 0
    total = 0

    for i in range(len(quiz)):
        if quiz[i] == 'X':
            score = 0
        elif score == 0:
            score = 1
        elif score != 0:
            score += 1

        total += score

    print(total)

'''
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
'''
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    rec = list(input().split())

    while True:
        words = list(map(str, input().split()))

        if words[0] == 'what':
            print(" ".join(rec))
            break

        while words[2] in rec:
            rec.remove(words[2])

from collections import defaultdict
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
count = 0

dict = defaultdict()

for i in range(a):
    if a_list[i] in dict.keys():
        dict[a_list[i]] += 1
    else:
        dict[a_list[i]] = 1

for i in range(b):
    if b_list[i] in dict.keys():
        dict[b_list[i]] += 1
    else:
        dict[b_list[i]] = 1

for d in dict:
    if dict[d] == 1:
        count += 1

print(count)
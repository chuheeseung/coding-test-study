a, b, c = map(int, input().split())

if c <= b:
    print(-1)
else:
    print(a//(c-b) + 1)



'''
1000 70 170
3 2 1
2100000000 9 10
'''
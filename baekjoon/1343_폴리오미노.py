import sys
input = sys.stdin.readline

board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)


'''
XXXXXX
AAAABB

XX.XX
BB.BB

XXXX....XXX.....XX
-1

X
-1

XX.XXXXXXXXXX..XXXXXXXX...XXXXXX
BB.AAAAAAAABB..AAAAAAAA...AAAABB
'''
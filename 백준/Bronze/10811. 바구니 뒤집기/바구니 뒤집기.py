import sys
a, b = map(int, sys.stdin.readline().split())
bk = [x+1 for x in range(a)]
for r in range(b):
    c, d = map(int, sys.stdin.readline().split())
    bk_r = bk[c-1:d][::-1]
    bk = bk[:c-1] + bk_r + bk[d:]

for x in range(len(bk)):
    print(bk[x], end=' ')
import sys

A = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
C = int(sys.stdin.readline())

D = 0
for i in range(A):
    if C == B[i]:
        D += 1

print(D)
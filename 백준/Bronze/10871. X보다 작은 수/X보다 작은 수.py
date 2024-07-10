import sys

A, B = map(int, sys.stdin.readline().split())
C = list(map(int, sys.stdin.readline().split()))

D = []
for i in range(A):
    if C[i] < B:
        D.append(C[i])

print(*D)
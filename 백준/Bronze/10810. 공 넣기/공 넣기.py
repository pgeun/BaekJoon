import sys

N, M = map(int, sys.stdin.readline().split())

basket = [0] * N

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    for j in range(A-1,B):
        basket[j] = C
        
for k in range(N):
    print(basket[k], end=" ")
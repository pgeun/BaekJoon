import sys

N, M = map(int, sys.stdin.readline().split())

basket = [0] * N

for j in range(N):
    basket[j] = j+1

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    basket[A-1], basket[B-1] = basket[B-1], basket[A-1]
        
for k in range(N):
    print(basket[k], end=" ")
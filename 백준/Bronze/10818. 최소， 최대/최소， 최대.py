import sys

A = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))

max = B[0]
min = B[0]
for i in range(1, A):
    if B[i] < min:
        min = int(B[i])
    else :
        continue
        
for i in range(1, A):
    if B[i] > max:
        max = int(B[i])
    else :
        continue

print(min,max)
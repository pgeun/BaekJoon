import sys

A = int(input())

for i in range(A):
    B,C = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i+1, B, C, B+C))
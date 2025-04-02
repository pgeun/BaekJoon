T = int(input())
C = [int(input()) for _ in range(T)]

for c in C:
    n=[0]*4
    n[0] = c//25
    c %= 25
    n[1] = c//10
    c %= 10
    n[2] = c//5
    c %= 5
    n[3] = c//1
    
    print(n[0], n[1], n[2], n[3])
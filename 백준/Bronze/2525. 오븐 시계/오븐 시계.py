A, B = map(int, input().split())
C = int(input())

D = B + C
if (D >= 60):
    E = D / 60
    A += E
    if (A >= 24):
        A -= 24
        print(int(A), int(D%60))
    else:
        print(int(A), int(D%60))
else :
    print(int(A), D)
A, B = map(int, input().split())

C = B - 45
if (C < 0):
    D = A-1
    B = 60 + C
    if (D<0):
        A = 24 + D
        print(A, B)
    else:
        print(D, B)
else :
    print(A, C)
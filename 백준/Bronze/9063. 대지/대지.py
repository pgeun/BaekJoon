num = int(input())

A, B = zip(*[map(int, input().split()) for _ in range(num)])
x1, x2, y1, y2 = min(A), max(A), min(B), max(B)

if len(A) == 1:
    print(0)
else:
    print((x2-x1)*(y2-y1))
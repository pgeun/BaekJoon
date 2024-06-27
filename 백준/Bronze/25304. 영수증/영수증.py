A = int(input())
B = int(input())

E = 0
while B != 0 :
    C, D = map(int, input().split())
    E += C * D
    B -= 1
if A==E:
    print('Yes')
else:
    print('No')
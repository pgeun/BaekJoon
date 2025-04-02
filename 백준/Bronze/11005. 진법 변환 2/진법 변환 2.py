N, B = map(int, input().split())
n=[]

while N>=B:
    n.append(N%B)
    N = N // B
n.append(N)

for _ in range(len(n)-1, -1, -1):
    if n[_] >=10 :
        print(chr(n[_]+55), end ='')
    else :
        print(n[_], end='')
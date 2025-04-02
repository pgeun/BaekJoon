N = int(input())
count = 1
result = 1

while result + count <= N:
    result += count
    count += 1

if count % 2 == 0:
    start = [count-1, 0]
    for _ in range(N-result):
        start[0] -= 1
        start[1] -= 1
else :
    start = [0, -(count-1)]
    for _ in range(N-result):
        start[0] += 1
        start[1] += 1
        
if count == 1:
    print('1/1')
else:
    for _ in range(2) :
        if start[_] < 0 :
            start[_] -= 1
        else:
            start[_] += 1
    print(abs(start[1]), end='')
    print('/', end='')
    print(abs(start[0]))
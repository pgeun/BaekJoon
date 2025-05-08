min = int(input())
max = int(input())
arr = []

for i in range(min, max+1):
    if i < 2:
        continue
    flag = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            flag = False
            break
    if flag :
        arr.append(i)    

if len(arr) == 0:
    print(-1)
else :
    print(sum(arr))
    print(arr[0])
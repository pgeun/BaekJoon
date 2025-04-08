num, index = map(int, input().split())
arr = []

for i in range(1, int(num/2)+2):
    if num%i == 0:
        arr.append(i)

arr.append(num)

if len(arr)<index:
    print('0')
else:
    print(arr[index-1])
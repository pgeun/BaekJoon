flag = True

while(flag):
    num = int(input())
    if num == -1:
        break
    arr = []
    sum = 0

    for i in range(1, int(num/2)+2):
        if num%i == 0:
            arr.append(i)
    for j in range(len(arr)):
        sum += arr[j]
    
    if sum == num:
        print(num, end='')
        print(' = ', end='')
        for k in range(len(arr)):
            if k==len(arr)-1:
                print(arr[k])
            else:
                print(arr[k],'+ ', end='')
    else :
        print(num,'is NOT perfect.')
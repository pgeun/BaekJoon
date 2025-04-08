flag = True

while(flag):
    num = int(input())
    if num == -1:
        break
    arr = []

    for i in range(1, int(num/2)+2):
        if num%i == 0:
            arr.append(i)
    
    if sum(arr) == num:
        print(num,' = ',' + '.join(str(i) for i in arr), sep='')
    else :
        print(num,'is NOT perfect.')
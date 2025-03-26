number = int(input())

word = [input() for i in range(number)]
result_count = 0

for w in word:
    count = 0
    flag = 0
    check = [0 for i in range(26)]
    for oa in w:
        count += 1
        if check[97-ord(oa)] == 0:
            check[97-ord(oa)] = count
        elif count - check[97-ord(oa)] == 1:
            check[97-ord(oa)] = count
        else :
            flag = 1
            break
        
    if flag == 0:
        result_count += 1

print(result_count)
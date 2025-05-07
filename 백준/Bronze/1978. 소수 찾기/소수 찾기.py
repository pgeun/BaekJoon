num = int(input())
num_l = list(map(int, input().split()))

count = len(num_l)

for i in num_l:
    if i == 1:
        count -= 1
        continue
    for j in range(2, int(i**(1/2)) + 1):
        if i % j == 0:
            count -= 1
            break

print(count)
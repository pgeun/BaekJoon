N = int(input())
count = 1
result = 1

while result < N:
    result += 6*count
    count += 1
    
print(count)
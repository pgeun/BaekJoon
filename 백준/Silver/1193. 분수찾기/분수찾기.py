N = int(input())
count = 1
result = 1

while result + count <= N:
    result += count
    count += 1

if count % 2 == 0:
    start = [(count-1)-(N-result), -(N-result)]
else :
    start = [(N-result), -(count-1)+(N-result)]

print(abs(start[1])+1, '/', abs(start[0])+1, sep='')
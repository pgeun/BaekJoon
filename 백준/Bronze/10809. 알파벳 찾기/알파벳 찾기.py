a = input()
b = [-1 for x in range(26)]

for i in range(len(a)):
    b[ord(a[i])-97] = a.find(a[i])

for j in range(len(b)):
    print(b[j], end=' ')
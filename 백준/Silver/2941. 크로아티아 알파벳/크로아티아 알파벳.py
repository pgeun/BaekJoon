A = input()
B = ''
C = ''

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in A:
    B += i
    for j in croatia:
        if j in B:
            count += 1
            B = B.replace(j,'')
            count += len(B)
            B = ''

print(count+len(B))
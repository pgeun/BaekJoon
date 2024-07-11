import sys

A = []
for i in range(9):
    A.append(int(sys.stdin.readline()))

max_value = A[0]
index = 1

for i in range(1, len(A)):
    if A[i] > max_value:
        max_value = A[i]
        index = i + 1

print(max_value)
print(index)
rows, cols = map(int, input().split())

arr = [list(map(int,input().split())) for i in range(rows)]
arr2 = [list(map(int,input().split())) for i in range(rows)]

arr3 = [[int(a) + int(b) for a, b in zip(row1, row2)] for row1, row2 in zip(arr, arr2)]

for i in range(rows):
    for j in range(cols):
        print(arr3[i][j], end=" ")
    print()
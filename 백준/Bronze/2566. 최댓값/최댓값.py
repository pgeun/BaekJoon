arr = [list(map(int, input().split())) for i in range(9)]

arr_max = 0
find_row, find_col = 0, 0

for i in range(9):
    for j in range(9):
        if arr[i][j] >= arr_max:
            arr_max = arr[i][j]
            find_row, find_col = i + 1, j + 1

print(arr_max)
print(find_row, find_col)
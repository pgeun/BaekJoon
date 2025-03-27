arr = [list(input()) for i in range(5)]

max_len = 0

for i in range(5):
    if max_len <= len(arr[i]):
        max_len = len(arr[i])

for i in range(5):
    if len(arr[i])<max_len:
        arr[i].extend([0]*(max_len-len(arr[i])))

for i in range(max_len):
    for j in range(5):
        if arr[j][i] != 0:
            print(arr[j][i], end='')
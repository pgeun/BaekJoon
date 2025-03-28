n = int(input())
paper = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    
    for y_ in range(y, y+10):
        for x_ in range(x, x+10):
            paper[y_][x_] = 1

width = 0
for k in range(100):
    width += paper[k].count(1)
    
print(width)
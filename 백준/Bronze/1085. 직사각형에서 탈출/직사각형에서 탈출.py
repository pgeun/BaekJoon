a, b, c, d = map(int, input().split())
x, y = c-a, d-b

result = min(a,b)
result = min(result, x)
result = min(result, y)

print(result)
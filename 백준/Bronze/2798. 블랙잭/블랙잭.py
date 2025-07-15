from itertools import combinations

num, line = map(int, input().split())
A = list(map(int, input().split()))

max_sum = 0
for combo in combinations(A, 3):
    total = sum(combo)
    if total <= line:
        max_sum = max(max_sum, total)

print(max_sum)
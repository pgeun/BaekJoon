from collections import Counter

A, B = zip(*[map(int, input().split()) for _ in range(3)])

a_counts = Counter(A)
b_counts = Counter(B)

unique_a = [x for x in A if a_counts[x] == 1]
unique_b = [x for x in B if b_counts[x] == 1]

print(unique_a[0], unique_b[0], sep =' ')
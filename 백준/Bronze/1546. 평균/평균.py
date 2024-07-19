import sys
a = sys.stdin.readline()
score = list(map(int, sys.stdin.readline().split()))
max = max(score)

for x in range(len(score)) :
    score[x] = score[x]/max*100

print(sum(score)/float(a))
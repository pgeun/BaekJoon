import sys
amount = int(sys.stdin.readline())
word = []
for i in range(amount):
    word.append(sys.stdin.readline())

for x in range(amount):
    print(word[x][0]+word[x][len(word[x])-2])
count = int(input())

for i in range(count):
    num,word = input().split()
    word_f = ''
    for r in range(len(word)):
        word_f += word[r]*int(num)
    print(word_f)
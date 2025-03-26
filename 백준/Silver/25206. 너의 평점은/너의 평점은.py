rows = 2
cols = 20
dict = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

sum = 0
sum2 = 0

for i in range(20):
    trach, score1, score2 = input().split()
    score1 = float(score1)
    if score2 != 'P':
        sum += score1 * dict[score2]
        sum2 += score1

result = sum / sum2
print(f"{result:.6f}")
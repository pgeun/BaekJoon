A = input()
sum = 0
number = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}
for n in A:
    for keys in number.keys():
        if n in keys:
            sum += number.get(keys)
print(sum)
side = [int(input()) for _ in range(3)]
hap = sum(side)

if hap == 180:
    side = set(side)
    if len(side) == 1:
        print('Equilateral')
    elif len(side) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
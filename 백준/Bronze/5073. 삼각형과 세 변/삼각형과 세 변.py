while (True):
    side = list(map(int,input().split()))
    side.sort()
    if sum(side) == 0:
        break
    if side[2]<side[0]+side[1]:
        unique = len(set(side))
        if unique == 3:
            print('Scalene')
        elif unique == 2:
            print('Isosceles')
        else:
            print('Equilateral')
    else:
        print('Invalid')
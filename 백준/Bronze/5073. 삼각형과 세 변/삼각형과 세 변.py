while (True):
    side = list(map(int,input().split()))
    side.sort()
    if sum(side) == 0:
        break
    if side[2]<side[0]+side[1]:
        side = sorted(set(side))
        if len(side) == 3:
            print('Scalene')
        elif len(side) == 2:
            print('Isosceles')
        else:
            print('Equilateral')
    else:
        print('Invalid')
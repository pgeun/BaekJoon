side = list(map(int,input().split()))
side.sort()
if side[2]>=side[0]+side[1]:
    diff = side[2]-(side[0]+side[1])
    side[2] = side[2]-diff-1
else:
    pass
print(sum(side))
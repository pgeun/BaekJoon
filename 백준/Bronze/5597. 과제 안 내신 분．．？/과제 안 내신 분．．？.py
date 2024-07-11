import sys

ad = [0] * 30

for i in range(28):
    A = int(sys.stdin.readline())
    ad[A-1] = A
    
for j in range(30):
    if ad[j] == 0:
        ad[j] = j+1
        print(ad[j])
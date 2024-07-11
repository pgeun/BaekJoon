import sys

ad = []
for i in range(10):
    A = int(sys.stdin.readline())
    ad.append(A%42)
    
print(len(set(ad)))
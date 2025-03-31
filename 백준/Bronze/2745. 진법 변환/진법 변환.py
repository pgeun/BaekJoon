N, B = input().split()
B = int(B)
total = 0
index = len(N)-1

for _ in range(len(N)):
    if not N[index-_].isdigit():
        total += (B**_)*(ord(N[index-_])-55)
    else:
        total += (B**_)*int(N[index-_])
        
print(total)
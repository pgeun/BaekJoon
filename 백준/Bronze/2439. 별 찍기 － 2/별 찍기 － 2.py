A = int(input())

for i in range(A):
    str1 = " " * (A-(i+1))
    str2 = "*" * (i+1)
    print(str1 + str2, end="\n")
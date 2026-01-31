n = int(input())
k = 10 ** (n-1)
p = (10 ** n)-1
for i in range(p, k-1, -1):
    if i%2 != 0:
        print(i)

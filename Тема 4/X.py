n = int(input())
k = 1
a = 0

for i in range(1, n+1):
	k = k * i
	a += k

print(a)

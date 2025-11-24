n = int(input())
k = 0
b = 0
a = 0

for i in range(1, n+1):
	if i != 1:
		a = int(input())
	k += i
	b += a

print(k-b)

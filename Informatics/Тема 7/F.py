n = int(input())
k = 1
a = 0
b = 0
while k < n:
	a += 1
	k = k * 2
print(a)
if n <= 0:
	print("0")
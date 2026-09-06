a, b = input().split()
a = int(a)
b = int(b)
x = a
y = b
i = 1
while x != y:
	i += 1
	if x > y:
		x = x - y
	elif x < y:
		y = y - x
print(x, i)
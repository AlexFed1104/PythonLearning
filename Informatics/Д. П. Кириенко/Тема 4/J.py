n = int(input())
k = 0
m = 0

for i in range(1, n):
	k = k + i*(i+1)
	if m == 0:
		m = str(i) + "*" + str(i + 1)
	else:
		m = str(m) + "+" + str(i) + "*" + str(i + 1)
print(m, k, sep="=")

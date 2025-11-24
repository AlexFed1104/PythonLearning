n = int(input())
m = 0
v = []

for i in range(1, n+1):
	m += 1
	for k in range(m):
		v.append(m)
print(*v[:n])

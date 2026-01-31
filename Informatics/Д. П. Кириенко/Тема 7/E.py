k = True
n = int(input())
while k < n:
	k = 2 * k
	if k == n:
		print("YES")
if k != n:
	print("NO")
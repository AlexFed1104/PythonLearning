a = int(input())
S = 1
for d in range(2,int(a**0.5)+1):
	if a % d == 0:
		S = S + d + a // d
if S == a:
	print("yes")
else:
	print("no")
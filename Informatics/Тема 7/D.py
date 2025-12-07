n = int(input())
i = 0
STEPEN = 0
print(1)
while STEPEN <= n:
	i += 1
	STEPEN = 2 ** i
	if STEPEN <= n:
		print(STEPEN)

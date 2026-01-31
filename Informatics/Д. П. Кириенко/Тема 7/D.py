n = int(input())
i = 0
STEPEN = 1
print(1)
while STEPEN <= n:
	i += 1
	STEPEN = 2 * STEPEN
	if STEPEN <= n:
		print(STEPEN)

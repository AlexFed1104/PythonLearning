n = int(input())
i = 0
breakit = False
while breakit == False:
	i += 1
	if n % i == 0 and i != 1:
		print(i)
		breakit = True

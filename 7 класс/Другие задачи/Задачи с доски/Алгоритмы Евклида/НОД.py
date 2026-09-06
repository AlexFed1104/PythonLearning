def NOD(a, b):
	x = a
	y = b
	while x != y:
		if x > y:
			x = x - y
		elif x < y:
			y = y - x
	return x
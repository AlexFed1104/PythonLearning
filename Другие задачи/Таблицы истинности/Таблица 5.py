print("x y z f")
for x in 0, 1:
	for y in 0, 1:
		for z in 0, 1:
			f = (x and y) or (not x and not z)
			print(x, y, z, int(f))
print("x y z f")
for x in 0, 1:
	for y in 0, 1:
		for z in 0, 1:
			for w in 0, 1:
				f = (not x and y == z) and w
				print(x, y, z, int(f))
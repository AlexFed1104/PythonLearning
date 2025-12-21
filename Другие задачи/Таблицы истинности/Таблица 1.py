print("x y z f")
for x in 0, 1:
	for y in 0, 1:
		for z in 0, 1:
			f = (z or y) <= (x==z)
			print(x, y, z, f)
k = 0
o = 0
t = 0

for k in range(1, 5):
	for o in range(0,10):
		for t in range(1,10):
			q = k*100+o*10+t*1
			w = k*100+t*10+o*1
			e = t*100+o*10+k*1
			if q + w == e:
				print(q,"+",w,"=",e)

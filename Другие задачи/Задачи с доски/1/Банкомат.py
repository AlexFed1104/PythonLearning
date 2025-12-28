"""
a = int(input())
if a%100:
	print('Ошибка')
v = a/100
b = int(v//5)
v = v-b*5
c = int(v//2)
v = int(v-c*2)

print(b, "купюр по 500", ",", c, "купюр по 200", ",", v, "купюр по 100")
"""
a = int(input())
for i in range(0, a//500+1):
	for k in range(0, a//200+1):
		for n in range(0, a//100+1):
			if i*500 + k*200 + n*100 == a:
				print(i, "купюр по 500", ",", k, "купюр по 200", ",", n, "купюр по 100")
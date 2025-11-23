from math import *
n = int(input())
k = int(input())
nf = factorial(n)
kf = factorial(k)
nkf = factorial(n-k)
print(int(nf / (kf * nkf)))
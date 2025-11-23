n = int(input())
if n == 1:
    print("+___ ")
    print("|1 / ")
    print("|__\\ ")
    print("|    ")

for i in range(n - 1):
    print("+___ ", end="")
    if i == n - 2:
        print("+___ ", end="\n")

for i in range(n - 1):
    print("|", i+1, " / ", end="", sep="")
    if i == n-2:
        print("|", i+2, " / ", end="\n", sep="")

for i in range(n - 1):
    print("|__\\ ", end="")
    if i == n - 2:
        print("|__\\ ", end="\n")

for i in range(n - 1):
    print("", end="|    ")
    if i == n - 2:
        print("|    ")

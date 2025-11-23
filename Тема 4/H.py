n =int(input())
if n == 1:
    print("   _~_    ")
    print("  (o o)   ")
    print(" /  V  \\  ")
    print("/(  _  )\\ ")
    print("  ^^ ^^   ")

for i in range(n-1):
    print("   _~_    ", end="")
    if i == n-2:
        print("   _~_   ", end="\n")

for i in range(n-1):
    print("  (o o)   ", end="")
    if i == n-2:
        print("  (o o)   ", end="\n")

for i in range(n-1):
    print(" /  V  \\  ", end="")
    if i == n-2:
       print(" /  V  \\  ", end="\n")

for i in range(n-1):
    print("/(  _  )\\ ", end="")
    if i == n-2:
       print("/(  _  )\\ ", end="\n")

for i in range(n-1):
    print("  ^^ ^^   ", end="")
    if i == n-2:
        print("  ^^ ^^   ", end="\n")

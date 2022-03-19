import math
a, b = input().split()

x = int(f'{a}{b}')

r = math.floor(math.sqrt(x))

if r*r == x:
    print("Yes")
else:
    print("No")
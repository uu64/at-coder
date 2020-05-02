import math
X = int(input())

year = 0
money = 100
while True:
    year += 1
    money = math.floor(money * 1.01)
    if money >= X:
        break

print(year)

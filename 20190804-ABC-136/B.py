# -*- coding: utf-8 -*-

N = input()

sum = 0
for i in range(1, len(N) + 1, 2):

    if int(N) >= 10 ** i:
        sum += (10**i - 1) - (10**(i - 1) - 1)
    else:
        sum += int(N) - (10**(i - 1) - 1)

print(sum)


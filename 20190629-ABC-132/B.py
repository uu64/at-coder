# -*- coding: utf-8 -*-

n = input()
p = list(map(int, input().split()))

counter = 0
for i in range(1, int(n) - 1):
    numbers = [p[i-1], p[i], p[i+1]]
    if sorted(numbers)[1] == p[i]:
        counter += 1

print(counter)
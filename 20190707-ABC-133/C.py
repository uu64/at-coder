# -*- coding: utf-8 -*-

L, R = map(int, input().split())

min = 2019

if R - L > 2019:
    R = L + 2019

for i in range(L, R+1):
    for j in range(i+1, R+1):
        mod = (i*j) % 2019
        if mod < min:
            min = mod

print(min)
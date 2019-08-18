# -*- coding: utf-8 -*-

N = int(input())
v = list(map(int, input().split()))

v = sorted(v)
a = v.pop(0)
b = v.pop(0)

result = (a + b)/2
while len(v) > 0:
    a = v.pop(0)
    b = result
    result = (a + b)/2

print(result)


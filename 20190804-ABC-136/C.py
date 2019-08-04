# -*- coding: utf-8 -*-

N = int(input())
H = list(map(int, input().split()))

max = -1
for i in H:
    if i - max < -1:
        print('No')
        exit(0)

    if max <= i:
        max = i

print('Yes')

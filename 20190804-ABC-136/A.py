# -*- coding: utf-8 -*-

A, B, C = map(int, input().split())

tmp = A - B

if tmp <= C:
    print(C - tmp)
else:
    print(0)

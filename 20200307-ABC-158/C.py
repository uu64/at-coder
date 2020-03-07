# -*- coding: utf-8 -*-
import math

A, B = map(int, input().split())

A_min = math.ceil(A / 0.08)
A_max = (A + 1) / 0.08

B_min = math.ceil(B / 0.1)
B_max = (B + 1) / 0.1

ans = max(A_min, B_min)
if ans < A_max and ans < B_max:
    print(ans)
else:
    print(-1)

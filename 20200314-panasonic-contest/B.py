# -*- coding: utf-8 -*-
import math

H, W = map(int, input().split())

ans = 0
if H == 1 or W == 1:
    ans = 1
else:
    q, mod = divmod(H, 2)
    if mod == 0:
        ans = W * q
    else:
        ans = W * q + math.ceil(W / 2)

print(ans)

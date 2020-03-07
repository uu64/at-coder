# -*- coding: utf-8 -*-

N, A, B = map(int, input().split())

q, mod = divmod(N, A + B)

print((A * q) + min(mod, A))

# -*- coding: utf-8 -*-
from decimal import *

a, b, c = map(int, input().split())

a = Decimal(a)
b = Decimal(b)
c = Decimal(c)

if a.sqrt() + b.sqrt() < c.sqrt():
    print("Yes")
else:
    print("No")

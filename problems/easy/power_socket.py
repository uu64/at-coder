#!/usr/bin/env python3

A, B = map(int, input().split())

count = 0
while A + (A-1)*(count-1) < B:
    count += 1

print(count)
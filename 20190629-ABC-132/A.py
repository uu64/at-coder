# -*- coding: utf-8 -*-

str_in = input()
str_set = set(str_in)

if len(str_in) != 4:
    print('No')
    quit()

if len(str_set) != 2:
    print('No')
    quit()

for s in str_set:
    if str_in.count(s) != 2:
        print('No')
        quit()

print('Yes')


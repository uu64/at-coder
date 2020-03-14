# -*- coding: utf-8 -*-

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

def get_str(seq_list):
    result = []
    for seq in seq_list:
        used_char_num = len(set(seq))
        for i in range(used_char_num + 1):
            result.append(seq + chars[i])
    return result

N = int(input())

seq_list = ["a"]
for i in range(N - 1):
    tmp = seq_list[:]
    seq_list = get_str(tmp)

for s in seq_list:
    print(s)

# -*- coding: utf-8 -*-
import math

def bin_search(num_list, threshold):
    len_half = int(len(num_list)/2)
    idx = len_half
    while True:
        if idx < 0:
            idx = 0
        if idx == len(num_list):
            idx = len(num_list) - 1

        if num_list[idx] >= threshold:
            if num_list[idx-1] < threshold:
                return idx
            else:
                len_half = math.ceil(len_half/2)
                offset = -len_half
        else:
            len_half = math.ceil(len_half/2)
            offset = len_half

        if idx == 0 or idx == len(num_list) - 1:
            return len(num_list)
        else:
            idx += offset

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a_sum = [a[0]]
    for i in range(1, N):
        a_sum.append(a_sum[i-1] + a[i])

    count = 0
    for i in range(N):
        if i == 0:
            idx = bin_search(a_sum, K)
        else:
            idx = bin_search(a_sum, K + a_sum[i-1])
        count += N - idx

    print(count)


if __name__ == "__main__":
    main()
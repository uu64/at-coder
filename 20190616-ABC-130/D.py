# -*- coding: utf-8 -*-

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0

    for start in range(N):
        max_len = N - start
        number = 0
        if number >= K:
            count += max_len
            break
        for str_len in range(0, max_len):
            number += a[start + str_len]
            if number >= K:
                count += max_len - str_len
                break

    print(count)


if __name__ == "__main__":
    main()
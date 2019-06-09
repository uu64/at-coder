# -*- coding: utf-8 -*-


def main():
    mod = 1000000007
    N, M = map(int, input().split())
    # 計算用にidx=-1を追加する
    a = [0 for i in range(0, N+2)]

    for i in range(M):
        a[int(input())+1] = -1

    a[1] = 1
    for i in range(2, N+2):
        if a[i] == -1:
            continue

        if a[i-1] != -1:
            a[i] += a[i-1]

        if a[i-2] != -1:
            a[i] += a[i-2]

        a[i] %= mod

    print(a[-1])


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    L.insert(0, -1)

    D = 0
    count = 1
    for i in range(2, N+2):
        D = D + L[i-1]
        if D > X:
            pass
        else:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
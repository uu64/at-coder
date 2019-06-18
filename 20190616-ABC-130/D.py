# -*- coding: utf-8 -*-

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    count = 0
    l_idx = 0
    r_idx = 0
    ruiseki_sum = 0
    while True:
        if ruiseki_sum < K:
            if r_idx < len(a):
                ruiseki_sum += a[r_idx]
                r_idx += 1
            else:
                break
        else:
            ruiseki_sum -= a[l_idx]
            l_idx += 1

        if ruiseki_sum >= K:
            count += N - r_idx + 1

        if r_idx == len(a) and l_idx == len(a):
            break

    print(count)


if __name__ == "__main__":
    main()

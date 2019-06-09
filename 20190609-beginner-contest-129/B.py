# -*- coding: utf-8 -*-


def main():
    N = input()
    inputs = list(map(int, input().split()))

    min = 100
    for i in range(1, int(N)):
        diff = abs(sum(inputs[:i]) - sum(inputs[i:]))
        if min > diff:
            min = diff

    print(min)


if __name__ == "__main__":
    main()
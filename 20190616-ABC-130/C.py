# -*- coding: utf-8 -*-

def main():
    W, H, x, y = map(int, input().split())

    x_c = W/2
    y_c = H/2

    S = W*H/2

    if x == x_c and y == y_c:
        print("{} {}".format(S, 1))
    elif x == x_c or y == y_c:
        print("{} {}".format(S, 0))
    else:
        print("{} {}".format(S, 0))


if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-

def main():
    inputs = list(map(int, input().split()))
    inputs.remove(max(inputs))
    print(sum(inputs))


if __name__ == "__main__":
    main()
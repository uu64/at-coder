import sys

S = input()

v = S.split("o")

if len(v) > 100000:
    print("No")
else:
    if len(v[0]) > 2 or len(v[-1]) > 2:
        print("No")
        sys.exit(0)

    for s in v[1:-1]:
        if len(s) != 2:
            print("No")
            sys.exit(0)
    print("Yes")
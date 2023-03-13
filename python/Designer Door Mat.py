"""
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
"""


def main(n, m):
    a = ".|."

    for i in range(n):
        if i % 2 == 0:
            print((a * i).center(m, "-"))

    print("WELCOME".center(m, "-"))


if __name__ == "__main__":
    n, m = map(int, input().split())

    main(n, m)

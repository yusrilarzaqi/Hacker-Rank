import os


def main(a: set, b: set) -> None:
    os.system("clear")
    [print(x) for x in a.symmetric_difference(b)]


if __name__ == "__main__":
    lenM = int(input())
    m = set(map(int, input().split()))
    lenN = int(input())
    n = set(map(int, input().split()))

    main(m, n)

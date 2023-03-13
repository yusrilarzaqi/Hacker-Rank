inputMany = lambda: set(map(int, input().split()))


def main(arr: list, a: set, b: set):
    """num = 0"""
    """ for i in arr: """
    """     if i in sorted(a): """
    """         print("+1") """
    """         num += 1 """
    """"""
    """     if i in sorted(b): """
    """         print("-1") """
    """         num -= 1 """

    return sum((i in a) - (i in b) for i in arr)


if __name__ == "__main__":
    n, m = input().split()
    arr = list(map(int, input().split()))
    a, b = inputMany(), inputMany()

    result = main(arr, a, b)

    print(result)

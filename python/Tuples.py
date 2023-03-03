if __name__ == "__main__":
    n = int(input())
    integer_separated = map(int, input().split())
    myTuple = tuple(integer_separated)

    print(hash(integer_separated))

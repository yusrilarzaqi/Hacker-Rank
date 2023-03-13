import textwrap


def wrap(string: str, max_width: int):
    return textwrap.fill(string, max_width)


if __name__ == "__main__":
    string, max_width = input("String: "), int(input("Max With: "))
    result = wrap(string, max_width)
    print(result)

## sample input
# abracadabra
# 5 k


def mutate_string(string: str, position: int, character: str) -> str:
    # return string[:position] + character + string[position + 1 :]
    result = list(string)

    result[position] = character

    return "".join(result)


if __name__ == "__main__":
    s = input("s: ")
    i, c = input("i & c: ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

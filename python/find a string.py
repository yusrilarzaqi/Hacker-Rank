## Example inputs
# ABCDCDC
# CDC
# 2


def count_substring(string: str, sub_string: str) -> int:
    result = 0

    while True:
        index = string.find(sub_string)

        if index == -1:
            break

        string = string[index + 1 :]
        result += 1

    return result


if __name__ == "__main__":
    string = input("string: ").strip()
    sub_string = input("sub string: ").strip()

    count = count_substring(string, sub_string)
    print(f"count: {count}")

def print_full_name(first: str, last: str) -> None:
    print(f"Hello {first} {last}! You just delved into python.")


if __name__ == "__main__":
    first = input()
    last = input()
    print_full_name(first, last)

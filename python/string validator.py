if __name__ == "__main__":
    string = input("string: ")

    alpha = alnum = digit = lower = upper = False

    for s in string:
        alpha = True if (s.isalpha() or alpha) else False
        alnum = True if (s.isalnum() or alnum) else False
        digit = True if (s.isdigit() or digit) else False
        lower = True if (s.islower() or lower) else False
        upper = True if (s.isupper() or upper) else False

    [print(x) for x in [alnum, alpha, digit, lower, upper]]

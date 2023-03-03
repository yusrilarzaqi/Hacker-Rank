if __name__ == "__main__":
    N = int(input(""))

    myList = []

    for _ in range(N):
        cmd = input("")

        if "insert" in cmd:
            split = cmd.split(" ")
            myList.insert(int(split[1]), int(split[2]))
        elif "print" in cmd:
            print(myList)
        elif "remove" in cmd:
            myList.remove(int(cmd.split(" ")[1]))
        elif "append" in cmd:
            myList.append(int(cmd.split(" ")[1]))
        elif "sort" in cmd:
            myList.sort()
        elif "pop" in cmd:
            myList.pop()
        elif "reverse" in cmd:
            myList.reverse()

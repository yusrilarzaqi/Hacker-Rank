thickness = 5
s = ""

for i in range(1, thickness * 2, 2):
    s = s + (i * "H").center(thickness * 2 - 1, " ") + "\n"

s1 = (thickness * "H").center(thickness * 2 - 1, " ") + (thickness * 2 + 1) * " "

for i in range(thickness + 1):
    s = s + (2 * s1) + "\n"

# middle line

s2 = (thickness * 5 * "h").center(thickness * 6 - 1, " ")

for i in range(0, thickness, 2):
    s = s + s2 + "\n"

# Bottom square

s3 = (thickness * "H").center(thickness * 2 - 1, " ") + (thickness * 2 + 1) * " "

for i in range(thickness + 1):
    s = s + (2 * s3) + "\n"

# Bottom cone

for i in range(thickness * 2 - 1, 0, -2):
    s = s + (thickness * 4) * " " + (i * "H").center(thickness * 2 - 1) + "\n"


print(s)

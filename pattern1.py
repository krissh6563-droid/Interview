n = int(input())
# First part: pyramid-like shape
for i in range(n // 2 + 1):
    for j in range(n // 2):
        print(" ", end="")
    for j in range(i):
        print(" ", end="")
    for j in range(n - (2 * i)):
        print("@", end="")
    print()
# Second part: row of '*' symbols
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == (n - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()